import tkinter as tk

class Pages:
    """Контейнер со страницами и навигацией (пагинация)
    
    Пример:
        >>> pages = Pages(app)
        >>> page1 = pages.add_page("Страница 1")
        >>> Label(page1, "Первая страница")
        >>> page2 = pages.add_page("Страница 2")
        >>> Input(page2, "Поле на второй странице")
    """
    
    def __init__(self, parent):
        """Инициализация контейнера со страницами
        
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
            
        self.pages = []
        self.current = 0
        
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.pages_frame = tk.Frame(self.main_frame)
        self.pages_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.prev_btn = tk.Button(self.buttons_frame, text="← Предыдущая", command=self.prev)
        self.prev_btn.pack(side=tk.LEFT, padx=2)
        
        self.next_btn = tk.Button(self.buttons_frame, text="Следующая →", command=self.next)
        self.next_btn.pack(side=tk.LEFT, padx=2)
        
        self.page_label = tk.Label(self.buttons_frame, text="Страница 1 из 1")
        self.page_label.pack(side=tk.LEFT, padx=20)
        
    def add_page(self, title):
        """Добавить новую страницу
        
        Args:
            title (str): Заголовок страницы
            
        Returns:
            tk.Frame: Фрейм страницы для размещения элементов
        """
        frame = tk.Frame(self.pages_frame)
        self.pages.append({
            'frame': frame,
            'title': title
        })
        
        if len(self.pages) == 1:
            frame.pack(fill=tk.BOTH, expand=True)
            
        self._update_nav()
        return frame
        
    def switch_to(self, index):
        """Переключиться на страницу по индексу
        
        Args:
            index (int): Индекс страницы
        """
        if 0 <= index < len(self.pages):
            self.pages[self.current]['frame'].pack_forget()
            self.current = index
            self.pages[self.current]['frame'].pack(fill=tk.BOTH, expand=True)
            self._update_nav()
            
    def prev(self):
        """Переключиться на предыдущую страницу"""
        if self.current > 0:
            self.switch_to(self.current - 1)
            
    def next(self):
        """Переключиться на следующую страницу"""
        if self.current < len(self.pages) - 1:
            self.switch_to(self.current + 1)
            
    def _update_nav(self):
        """Обновить состояние кнопок навигации"""
        total = len(self.pages)
        self.page_label.config(text=f"Страница {self.current + 1} из {total}")
        
        self.prev_btn.config(state=tk.NORMAL if self.current > 0 else tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL if self.current < total - 1 else tk.DISABLED)