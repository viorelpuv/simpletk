import tkinter as tk

class Utils:
    """Вспомогательные утилиты
    
    Пример:
        >>> Utils.center_window(app.root, 800, 600)
    """
    
    @staticmethod
    def center_window(window, width, height):
        """Центрировать окно на экране
        
        Args:
            window: Окно tkinter
            width (int): Ширина окна
            height (int): Высота окна
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")