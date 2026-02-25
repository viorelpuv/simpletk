import tkinter as tk

class Label:
    """Текстовая метка
    
    Пример:
        >>> label = Label(app, "Привет, мир!", size=14, bold=True, color="blue")
    """
    
    def __init__(self, parent, text="Text", size=12, bold=False, color="black"):
        """Инициализация метки
        
        Args:
            parent: Родительский элемент
            text (str): Текст метки
            size (int): Размер шрифта
            bold (bool): Жирный шрифт
            color (str): Цвет текста
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        font = ("Arial", size, "bold" if bold else "normal")
        self.widget = tk.Label(self.parent, text=text, font=font, fg=color)
        self.widget.pack(pady=2)
        
    def set_text(self, text):
        """Изменить текст
        
        Args:
            text (str): Новый текст
        """
        self.widget.config(text=text)
        
    def set_color(self, color):
        """Изменить цвет текста
        
        Args:
            color (str): Новый цвет
        """
        self.widget.config(fg=color)
        
    def hide(self):
        """Скрыть метку"""
        self.widget.pack_forget()
        
    def show(self):
        """Показать метку"""
        self.widget.pack(pady=2)