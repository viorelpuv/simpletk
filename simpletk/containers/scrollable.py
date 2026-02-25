import tkinter as tk

class ScrollableFrame(tk.Frame):
    """
    Универсальный прокручиваемый контейнер.
    
    Пример:
        >>> scroll = ScrollableFrame(app)
        >>> scroll.pack(fill=tk.BOTH, expand=True)
        >>> for i in range(50):
        ...     Label(scroll.scrollable_frame, f"Строка {i}")
    """
    
    def __init__(self, parent, width=None, height=None, bg=None, **kwargs):
        """
        Инициализация прокручиваемого контейнера
        
        Args:
            parent: Родительский элемент
            width (int): Ширина области просмотра
            height (int): Высота области просмотра
            bg (str): Цвет фона
            **kwargs: Дополнительные аргументы для tk.Frame
        """
        # Получаем реальный tkinter widget от родителя
        if hasattr(parent, 'frame'):
            master = parent.frame
        elif hasattr(parent, 'root'):
            master = parent.root
        else:
            master = parent
            
        # Инициализируем Frame
        super().__init__(master, **kwargs)
        
        # Создаём Canvas
        self.canvas = tk.Canvas(self, bg=bg, highlightthickness=0)
        
        # Создаём вертикальный scrollbar
        self.v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)
        
        # Упаковываем scrollbar и canvas
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Устанавливаем размеры canvas
        if width:
            self.canvas.config(width=width)
        if height:
            self.canvas.config(height=height)
        
        # Создаём внутренний фрейм для содержимого - ЭТОТ ФРЕЙМ НУЖНО ИСПОЛЬЗОВАТЬ
        self.scrollable_frame = tk.Frame(self.canvas, bg=bg)
        
        # Создаём окно в canvas
        self.canvas_window = self.canvas.create_window(
            (0, 0), 
            window=self.scrollable_frame, 
            anchor="nw"
        )
        
        # Привязываем события
        self.scrollable_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        
        # Привязываем колесо мыши
        self._bind_mousewheel()
        
    def _on_frame_configure(self, event):
        """Обновление области прокрутки при изменении внутреннего фрейма"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def _on_canvas_configure(self, event):
        """Изменение ширины внутреннего фрейма при изменении canvas"""
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)
        
    def _bind_mousewheel(self):
        """Привязка колеса мыши к прокрутке"""
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # Привязываем к canvas и всем дочерним элементам
        self.canvas.bind("<MouseWheel>", _on_mousewheel)
        self.scrollable_frame.bind("<MouseWheel>", _on_mousewheel)
        
    def scroll_to_top(self):
        """Прокрутить вверх"""
        self.canvas.yview_moveto(0)
        
    def scroll_to_bottom(self):
        """Прокрутить вниз"""
        self.canvas.yview_moveto(1)
        
    def clear(self):
        """Очистить все элементы из внутреннего фрейма"""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()