import tkinter as tk

class RadioGroup:
    """Группа радиокнопок
    
    Пример:
        >>> gender = RadioGroup(app, ["Мужской", "Женский", "Другой"])
        >>> selected = gender.get()
        >>> gender.set("Женский")
    """
    
    def __init__(self, parent, options, on_change=None):
        """Инициализация группы радиокнопок
        
        Args:
            parent: Родительский элемент
            options (list): Список опций
            on_change (callable): Функция, вызываемая при изменении выбора
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        self.value = tk.StringVar()
        self.value.set(options[0] if options else "")
        self.buttons = []
        
        for option in options:
            rb = tk.Radiobutton(self.parent, text=option, variable=self.value,
                               value=option, command=on_change)
            rb.pack(pady=1)
            self.buttons.append(rb)
            
    def get(self):
        """Получить выбранную опцию
        
        Returns:
            str: Выбранная опция
        """
        return self.value.get()
        
    def set(self, option):
        """Установить выбранную опцию
        
        Args:
            option (str): Опция для выбора
        """
        self.value.set(option)
        
    def hide(self):
        """Скрыть все радиокнопки"""
        for btn in self.buttons:
            btn.pack_forget()
        
    def show(self):
        """Показать все радиокнопки"""
        for btn in self.buttons:
            btn.pack(pady=1)