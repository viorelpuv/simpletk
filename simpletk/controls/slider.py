import tkinter as tk

class Slider:
    """Ползунок для выбора числа
    
    Пример:
        >>> volume = Slider(app, from_=0, to=100, on_change=lambda v: print(f"Громкость: {v}"))
        >>> value = volume.get()
        >>> volume.set(50)
    """
    
    def __init__(self, parent, from_=0, to=100, on_change=None):
        """Инициализация ползунка
        
        Args:
            parent: Родительский элемент
            from_ (int): Минимальное значение
            to (int): Максимальное значение
            on_change (callable): Функция, вызываемая при изменении
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        self.value = tk.IntVar()
        self.widget = tk.Scale(self.parent, from_=from_, to=to, orient=tk.HORIZONTAL,
                               variable=self.value, command=on_change)
        self.widget.pack(fill=tk.X, pady=2)
        
    def get(self):
        """Получить текущее значение
        
        Returns:
            int: Текущее значение
        """
        return self.value.get()
        
    def set(self, value):
        """Установить значение
        
        Args:
            value (int): Новое значение
        """
        self.value.set(value)
        
    def hide(self):
        """Скрыть ползунок"""
        self.widget.pack_forget()
        
    def show(self):
        """Показать ползунок"""
        self.widget.pack(fill=tk.X, pady=2)