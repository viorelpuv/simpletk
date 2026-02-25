import tkinter as tk

class Vertical:
    """Вертикальный контейнер для размещения элементов в колонку
    
    Пример:
        >>> col = Vertical(app)
        >>> Label(col, "Заголовок")
        >>> Input(col, "Поле 1")
        >>> Input(col, "Поле 2")
        >>> Button(col, "Отправить")
    """
    
    def __init__(self, parent):
        """Инициализация вертикального контейнера
        
        Args:
            parent: Родительский элемент
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
        
    def add(self, element):
        """Добавить элемент в вертикальный контейнер
        
        Args:
            element: Элемент для добавления
        """
        if hasattr(element, 'widget'):
            element.widget.pack(in_=self.frame, fill=tk.X, pady=2)
        else:
            element.pack(in_=self.frame, fill=tk.X, pady=2)