import tkinter as tk

class Button:
    """Простая кнопка
    
    Пример:
        >>> def click_handler():
        ...     print("Кнопка нажата!")
        >>> btn = Button(app, "Нажми меня", on_click=click_handler, color="lightblue")
    """
    
    def __init__(self, parent, text="Button", on_click=None, color="lightgray"):
        """Инициализация кнопки
        
        Args:
            parent: Родительский элемент (App или контейнер)
            text (str): Текст на кнопке
            on_click (callable): Функция, вызываемая при нажатии
            color (str): Цвет кнопки
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        self.widget = tk.Button(self.parent, text=text, command=on_click, bg=color)
        self.widget.pack(pady=2)
        
    def set_text(self, text):
        """Изменить текст на кнопке
        
        Args:
            text (str): Новый текст
        """
        self.widget.config(text=text)
        
    def set_color(self, color):
        """Изменить цвет кнопки
        
        Args:
            color (str): Новый цвет
        """
        self.widget.config(bg=color)
        
    def hide(self):
        """Скрыть кнопку"""
        self.widget.pack_forget()
        
    def show(self):
        """Показать кнопку"""
        self.widget.pack(pady=2)