import tkinter as tk
from tkinter import ttk

class Tabs:
    """Контейнер с вкладками
    
    Пример:
        >>> tabs = Tabs(app)
        >>> tab1 = tabs.add("Вкладка 1")
        >>> Label(tab1, "Содержимое вкладки 1")
        >>> tab2 = tabs.add("Вкладка 2")
        >>> Button(tab2, "Кнопка на вкладке 2")
    """
    
    def __init__(self, parent):
        """Инициализация контейнера с вкладками
        
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
            
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def add(self, title):
        """Добавить новую вкладку
        
        Args:
            title (str): Заголовок вкладки
            
        Returns:
            tk.Frame: Фрейм вкладки для размещения элементов
        """
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text=title)
        return frame