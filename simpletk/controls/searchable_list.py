import tkinter as tk

class SearchableList:
    """Список с расширенными возможностями поиска и сортировки
    
    Пример:
        >>> slist = SearchableList(app, items=[
        ...     "Яблоко", "Банан", "Апельсин", "Груша", "Арбуз"
        ... ])
        >>> slist.search("а")  # Поиск элементов с буквой 'а'
        >>> slist.search_startswith("А")  # Поиск элементов на 'А'
        >>> slist.sort_by_length()  # Сортировка по длине
    """
    
    def __init__(self, parent, items, height=5, show_controls=True):
        """Инициализация списка с поиском
        
        Args:
            parent: Родительский элемент
            items (list): Список элементов
            height (int): Высота списка
            show_controls (bool): Показывать панель управления
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        elif hasattr(parent, 'scrollable_frame'):
            self.parent = parent.scrollable_frame
        else:
            self.parent = parent
            
        self.all_items = items.copy()
        self.displayed_items = items.copy()
        
        # Создаём основной контейнер
        self.container = tk.Frame(self.parent)
        self.container.pack(fill=tk.BOTH, expand=True, pady=2)
        
        if show_controls:
            self._create_control_panel()
        
        # Создаём Listbox с прокруткой
        self._create_listbox(height)
        
    def _create_control_panel(self):
        """Создание панели управления"""
        self.control_frame = tk.Frame(self.container)
        self.control_frame.pack(fill=tk.X, pady=(0, 2))
        
        # Поиск
        search_frame = tk.Frame(self.control_frame)
        search_frame.pack(fill=tk.X, pady=1)
        
        tk.Label(search_frame, text="🔍 Поиск:").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        self.search_entry.bind('<KeyRelease>', self._on_search)
        
        tk.Button(search_frame, text="✕", command=self.clear_search,
                 font=("Arial", 8), width=2).pack(side=tk.LEFT)
        
        # Кнопки сортировки
        sort_frame = tk.Frame(self.control_frame)
        sort_frame.pack(fill=tk.X, pady=1)
        
        tk.Button(sort_frame, text="А→Я", command=self.sort_ascending,
                 font=("Arial", 8), width=5).pack(side=tk.LEFT, padx=1)
        tk.Button(sort_frame, text="Я→А", command=self.sort_descending,
                 font=("Arial", 8), width=5).pack(side=tk.LEFT, padx=1)
        tk.Button(sort_frame, text="По длине ↑", command=self.sort_by_length_asc,
                 font=("Arial", 8), width=8).pack(side=tk.LEFT, padx=1)
        tk.Button(sort_frame, text="По длине ↓", command=self.sort_by_length_desc,
                 font=("Arial", 8), width=8).pack(side=tk.LEFT, padx=1)
        
        # Кнопки поиска по началу
        search_type_frame = tk.Frame(self.control_frame)
        search_type_frame.pack(fill=tk.X, pady=1)
        
        tk.Button(search_type_frame, text="Начинается с", 
                 command=self._search_startswith_dialog,
                 font=("Arial", 8)).pack(side=tk.LEFT, padx=1)
        tk.Button(search_type_frame, text="Заканчивается на", 
                 command=self._search_endswith_dialog,
                 font=("Arial", 8)).pack(side=tk.LEFT, padx=1)
        
        # Информация
        self.info_label = tk.Label(self.control_frame, 
                                   text=f"Всего: {len(self.all_items)}", 
                                   font=("Arial", 7))
        self.info_label.pack(pady=1)
        
    def _create_listbox(self, height):
        """Создание списка с прокруткой"""
        listbox_frame = tk.Frame(self.container)
        listbox_frame.pack(fill=tk.BOTH, expand=True)
        
        self.widget = tk.Listbox(listbox_frame, height=height)
        self.scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.widget.yview)
        self.widget.configure(yscrollcommand=self.scrollbar.set)
        
        self.widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self._update_display()
        
    def _update_display(self):
        """Обновление отображения"""
        self.widget.delete(0, tk.END)
        for item in self.displayed_items:
            self.widget.insert(tk.END, item)
        
        if hasattr(self, 'info_label'):
            self.info_label.config(text=f"Найдено: {len(self.displayed_items)} из {len(self.all_items)}")
        
    def _on_search(self, event=None):
        """Обработка поиска"""
        text = self.search_entry.get().lower()
        if text:
            self.displayed_items = [item for item in self.all_items if text in item.lower()]
        else:
            self.displayed_items = self.all_items.copy()
        self._update_display()
        
    def _search_startswith_dialog(self):
        """Диалог для поиска по началу строки"""
        dialog = tk.Toplevel(self.parent)
        dialog.title("Поиск по началу")
        dialog.geometry("300x100")
        
        tk.Label(dialog, text="Введите начало строки:").pack(pady=5)
        entry = tk.Entry(dialog, width=20)
        entry.pack(pady=5)
        
        def do_search():
            text = entry.get()
            if text:
                self.search_startswith(text)
            dialog.destroy()
        
        tk.Button(dialog, text="Поиск", command=do_search).pack()
        
    def _search_endswith_dialog(self):
        """Диалог для поиска по концу строки"""
        dialog = tk.Toplevel(self.parent)
        dialog.title("Поиск по концу")
        dialog.geometry("300x100")
        
        tk.Label(dialog, text="Введите конец строки:").pack(pady=5)
        entry = tk.Entry(dialog, width=20)
        entry.pack(pady=5)
        
        def do_search():
            text = entry.get()
            if text:
                self.search_endswith(text)
            dialog.destroy()
        
        tk.Button(dialog, text="Поиск", command=do_search).pack()
        
    # Методы сортировки
    def sort_ascending(self):
        """Сортировка по возрастанию"""
        self.displayed_items.sort()
        self._update_display()
        
    def sort_descending(self):
        """Сортировка по убыванию"""
        self.displayed_items.sort(reverse=True)
        self._update_display()
        
    def sort_by_length_asc(self):
        """Сортировка по длине (возрастание)"""
        self.displayed_items.sort(key=len)
        self._update_display()
        
    def sort_by_length_desc(self):
        """Сортировка по длине (убывание)"""
        self.displayed_items.sort(key=len, reverse=True)
        self._update_display()
        
    def sort_by(self, key_func, reverse=False):
        """Сортировка по пользовательской функции
        
        Args:
            key_func: Функция для получения ключа сортировки
            reverse (bool): Сортировка по убыванию
        """
        self.displayed_items.sort(key=key_func, reverse=reverse)
        self._update_display()
        
    # Методы поиска
    def search(self, text):
        """Поиск по тексту (содержит подстроку)
        
        Args:
            text (str): Текст для поиска
        """
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, text)
        self._on_search()
        
    def search_startswith(self, prefix):
        """Поиск по началу строки
        
        Args:
            prefix (str): Начало строки
        """
        prefix = prefix.lower()
        self.displayed_items = [item for item in self.all_items 
                               if item.lower().startswith(prefix)]
        self._update_display()
        
    def search_endswith(self, suffix):
        """Поиск по концу строки
        
        Args:
            suffix (str): Конец строки
        """
        suffix = suffix.lower()
        self.displayed_items = [item for item in self.all_items 
                               if item.lower().endswith(suffix)]
        self._update_display()
        
    def search_by_length(self, min_len=None, max_len=None):
        """Поиск по длине строки
        
        Args:
            min_len (int): Минимальная длина
            max_len (int): Максимальная длина
        """
        def check_length(item):
            if min_len and len(item) < min_len:
                return False
            if max_len and len(item) > max_len:
                return False
            return True
            
        self.displayed_items = [item for item in self.all_items if check_length(item)]
        self._update_display()
        
    def search_custom(self, search_func):
        """Поиск по пользовательской функции
        
        Args:
            search_func: Функция, возвращающая True для элементов, которые нужно показать
        """
        self.displayed_items = [item for item in self.all_items if search_func(item)]
        self._update_display()
        
    def clear_search(self):
        """Сброс всех поисковых запросов"""
        self.search_entry.delete(0, tk.END)
        self.displayed_items = self.all_items.copy()
        self._update_display()
        
    # Базовые методы
    def add_item(self, item):
        """Добавить элемент"""
        self.all_items.append(item)
        self.clear_search()
        
    def add_items(self, items):
        """Добавить несколько элементов"""
        self.all_items.extend(items)
        self.clear_search()
        
    def remove_selected(self):
        """Удалить выбранный элемент"""
        selection = self.widget.curselection()
        if selection:
            index = selection[0]
            item = self.displayed_items[index]
            self.all_items.remove(item)
            self.displayed_items.pop(index)
            self._update_display()
            
    def get_selected(self):
        """Получить выбранный элемент"""
        selection = self.widget.curselection()
        if selection:
            return self.displayed_items[selection[0]]
        return None
        
    def clear(self):
        """Очистить список"""
        self.all_items = []
        self.displayed_items = []
        self._update_display()