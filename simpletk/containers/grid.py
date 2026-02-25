import tkinter as tk

class Grid:
    """Сеточный контейнер для размещения элементов в таблицу
    
    Пример:
        >>> grid = Grid(app, rows=3, cols=3)
        >>> for i in range(9):
        ...     Button(grid, f"Кнопка {i+1}")
    """
    
    def __init__(self, parent, rows=3, cols=3):
        """Инициализация сеточного контейнера
        
        Args:
            parent: Родительский элемент
            rows (int): Количество строк
            cols (int): Количество колонок
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
        
        for i in range(rows):
            self.frame.grid_rowconfigure(i, weight=1)
        for i in range(cols):
            self.frame.grid_columnconfigure(i, weight=1)
            
        self.current_row = 0
        self.current_col = 0
        self.max_cols = cols
        
    def add(self, element):
        """Добавить элемент в сетку
        
        Args:
            element: Элемент для добавления
        """
        if hasattr(element, 'widget'):
            element.widget.grid(in_=self.frame, row=self.current_row, 
                               column=self.current_col, padx=2, pady=2, sticky="nsew")
        else:
            element.grid(in_=self.frame, row=self.current_row, 
                        column=self.current_col, padx=2, pady=2, sticky="nsew")
        
        self.current_col += 1
        if self.current_col >= self.max_cols:
            self.current_col = 0
            self.current_row += 1