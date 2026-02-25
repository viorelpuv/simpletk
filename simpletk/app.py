import tkinter as tk
from tkinter import messagebox, filedialog

class App:
    """Главное окно приложения
    
    Основной класс для создания окна приложения.
    
    Пример:
        >>> app = App("Моё приложение", 800, 600)
        >>> app.run()
    """
    
    def __init__(self, title="My Application", width=800, height=600):
        """Инициализация главного окна
        
        Args:
            title (str): Заголовок окна
            width (int): Ширина окна
            height (int): Высота окна
        """
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.elements = []
        
    def run(self):
        """Запуск приложения (главный цикл обработки событий)"""
        self.root.mainloop()
        
    def close(self):
        """Закрытие приложения"""
        self.root.quit()
        
    def set_size(self, width, height):
        """Установка размера окна
        
        Args:
            width (int): Новая ширина
            height (int): Новая высота
        """
        self.root.geometry(f"{width}x{height}")
        
    def set_title(self, title):
        """Установка заголовка окна
        
        Args:
            title (str): Новый заголовок
        """
        self.root.title(title)
        
    def center(self):
        """Центрирование окна на экране"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def message(self, text, title="Message"):
        """Показать информационное сообщение
        
        Args:
            text (str): Текст сообщения
            title (str): Заголовок окна
        """
        messagebox.showinfo(title, text)
        
    def question(self, text, title="Question"):
        """Задать вопрос с ответом Да/Нет
        
        Args:
            text (str): Текст вопроса
            title (str): Заголовок окна
            
        Returns:
            bool: True если пользователь нажал "Да", иначе False
        """
        return messagebox.askyesno(title, text)
        
    def warning(self, text, title="Warning"):
        """Показать предупреждение
        
        Args:
            text (str): Текст предупреждения
            title (str): Заголовок окна
        """
        messagebox.showwarning(title, text)
        
    def error(self, text, title="Error"):
        """Показать сообщение об ошибке
        
        Args:
            text (str): Текст ошибки
            title (str): Заголовок окна
        """
        messagebox.showerror(title, text)
        
    def open_file(self, filetypes=[("All files", "*.*")]):
        """Диалог выбора файла
        
        Args:
            filetypes (list): Список кортежей (описание, расширение)
            
        Returns:
            str: Путь к выбранному файлу или пустая строка
        """
        return filedialog.askopenfilename(filetypes=filetypes)
        
    def open_folder(self):
        """Диалог выбора папки
        
        Returns:
            str: Путь к выбранной папке или пустая строка
        """
        return filedialog.askdirectory()