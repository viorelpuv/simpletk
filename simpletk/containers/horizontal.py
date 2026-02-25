import tkinter as tk

class Horizontal:
    """Горизонтальный контейнер для размещения элементов в ряд
    
    Пример:
        >>> row = Horizontal(app)
        >>> Label(row, "Имя:")
        >>> Input(row, "Введите имя")
        >>> Button(row, "ОК")
    """
    
    def __init__(self, parent):
        """Инициализация горизонтального контейнера
        
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
        self.frame.pack(fill=tk.X, padx=5, pady=5)
        
    def add(self, element):
        """Добавить элемент в горизонтальный контейнер
        
        Args:
            element: Элемент для добавления (Button, Label, Input и т.д.)
        """
        if hasattr(element, 'widget'):
            element.widget.pack(in_=self.frame, side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        else:
            element.pack(in_=self.frame, side=tk.LEFT, expand=True, fill=tk.X, padx=2)