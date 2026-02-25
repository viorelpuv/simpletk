import tkinter as tk

class Checkbox:
    """Флажок (чекбокс)
    
    Пример:
        >>> cb = Checkbox(app, "Согласен", on_change=lambda: print(cb.is_checked()))
        >>> if cb.is_checked():
        ...     print("Отмечено")
    """
    
    def __init__(self, parent, text="Check", on_change=None):
        """Инициализация чекбокса
        
        Args:
            parent: Родительский элемент
            text (str): Текст рядом с чекбоксом
            on_change (callable): Функция, вызываемая при изменении состояния
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        self.value = tk.BooleanVar()
        self.widget = tk.Checkbutton(self.parent, text=text, variable=self.value, command=on_change)
        self.widget.pack(pady=2)
        
    def is_checked(self):
        """Проверить, отмечен ли чекбокс
        
        Returns:
            bool: True если отмечен, иначе False
        """
        return self.value.get()
        
    def set_checked(self, checked=True):
        """Установить состояние
        
        Args:
            checked (bool): Новое состояние
        """
        self.value.set(checked)
        
    def hide(self):
        """Скрыть чекбокс"""
        self.widget.pack_forget()
        
    def show(self):
        """Показать чекбокс"""
        self.widget.pack(pady=2)