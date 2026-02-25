import tkinter as tk

class Input:
    """Поле ввода текста
    
    Пример:
        >>> name_input = Input(app, "Введите имя", width=30)
        >>> name = name_input.get()
        >>> name_input.set("Новый текст")
    """
    
    def __init__(self, parent, placeholder="", width=30):
        """Инициализация поля ввода
        
        Args:
            parent: Родительский элемент
            placeholder (str): Текст-подсказка
            width (int): Ширина поля
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        self.widget = tk.Entry(self.parent, width=width)
        self.widget.pack(pady=2)
        
        if placeholder:
            self.widget.insert(0, placeholder)
            self.widget.bind('<FocusIn>', lambda e: self._clear_placeholder(placeholder))
            
    def _clear_placeholder(self, placeholder):
        if self.widget.get() == placeholder:
            self.widget.delete(0, tk.END)
            
    def get(self):
        """Получить введённый текст
        
        Returns:
            str: Текст из поля ввода
        """
        return self.widget.get()
        
    def set(self, text):
        """Установить текст
        
        Args:
            text (str): Новый текст
        """
        self.widget.delete(0, tk.END)
        self.widget.insert(0, text)
        
    def clear(self):
        """Очистить поле"""
        self.widget.delete(0, tk.END)
        
    def hide(self):
        """Скрыть поле"""
        self.widget.pack_forget()
        
    def show(self):
        """Показать поле"""
        self.widget.pack(pady=2)