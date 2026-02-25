import tkinter as tk

class ScrollArea:
    """Область с прокруткой для размещения большого количества элементов
    
    Пример:
        >>> scroll = ScrollArea(app, height=200, width=400)
        >>> for i in range(50):
        ...     Label(scroll, f"Строка {i+1}")
    """
    
    def __init__(self, parent, height=200, width=400):
        """Инициализация области с прокруткой
        
        Args:
            parent: Родительский элемент
            height (int): Высота области
            width (int): Ширина области
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
        
        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create canvas and scrollbars
        self.canvas = tk.Canvas(self.frame, height=height, width=width)
        self.v_scroll = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.h_scroll = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)
        
        # Use pack instead of grid to avoid geometry manager conflict
        self.v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Inner frame for content
        self.inner = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        
        # Bind events
        self.inner.bind("<Configure>", self._update_scroll)
        self.canvas.bind("<Configure>", self._resize_inner)
        
    def _update_scroll(self, event):
        """Обновить область прокрутки при изменении внутреннего фрейма"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def _resize_inner(self, event):
        """Изменить размер внутреннего фрейма при изменении canvas"""
        canvas_width = event.width
        self.canvas.itemconfig(1, width=canvas_width)  # 1 is the window id of inner frame
        
    def add(self, element):
        """Добавить элемент в область с прокруткой
        
        Args:
            element: Элемент для добавления
        """
        if hasattr(element, 'widget'):
            element.widget.pack(in_=self.inner, fill=tk.X, pady=1)
        else:
            element.pack(in_=self.inner, fill=tk.X, pady=1)