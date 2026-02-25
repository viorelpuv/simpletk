'''import tkinter as tk

class ListBox:
    """Список для выбора элементов
    
    Пример:
        >>> listbox = ListBox(app, ["Яблоко", "Банан", "Апельсин"], height=5)
        >>> selected = listbox.get_selected()
        >>> listbox.add_item("Виноград")
    """
    
    def __init__(self, parent, items, height=5):
        """Инициализация списка
        
        Args:
            parent: Родительский элемент
            items (list): Список элементов
            height (int): Высота списка в строках
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        self.widget = tk.Listbox(self.parent, height=height)
        self.widget.pack(fill=tk.BOTH, expand=True, pady=2)
        
        for item in items:
            self.widget.insert(tk.END, item)
            
    def get_selected(self):
        """Получить выбранный элемент
        
        Returns:
            str or None: Выбранный элемент или None
        """
        selection = self.widget.curselection()
        if selection:
            return self.widget.get(selection[0])
        return None
        
    def add_item(self, item):
        """Добавить элемент в список
        
        Args:
            item (str): Новый элемент
        """
        self.widget.insert(tk.END, item)
        
    def remove_selected(self):
        """Удалить выбранный элемент"""
        selection = self.widget.curselection()
        if selection:
            self.widget.delete(selection[0])
            
    def clear(self):
        """Очистить список"""
        self.widget.delete(0, tk.END)
        
    def hide(self):
        """Скрыть список"""
        self.widget.pack_forget()
        
    def show(self):
        """Показать список"""
        self.widget.pack(fill=tk.BOTH, expand=True, pady=2)
'''

import tkinter as tk

class ListBox:
    """Список для выбора элементов с поддержкой сортировки и поиска
    
    Пример:
        >>> listbox = ListBox(app, ["Яблоко", "Банан", "Апельсин"], height=5)
        >>> listbox.sort()  # Сортировка по алфавиту
        >>> listbox.search("а")  # Поиск: показать только элементы с буквой 'а'
        >>> listbox.clear_search()  # Сброс поиска
    """
    
    def __init__(self, parent, items, height=5, sortable=True, searchable=True):
        """Инициализация списка
        
        Args:
            parent: Родительский элемент
            items (list): Список элементов
            height (int): Высота списка в строках
            sortable (bool): Возможность сортировки
            searchable (bool): Возможность поиска (ИСПРАВЛЕНО: searchable, а не searchable)
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        elif hasattr(parent, 'scrollable_frame'):  # Для ScrollableFrame
            self.parent = parent.scrollable_frame
        else:
            self.parent = parent
            
        self.all_items = items.copy()  # Все элементы (оригинал)
        self.displayed_items = items.copy()  # Отображаемые элементы
        self.sortable = sortable
        self.searchable = searchable  # ИСПРАВЛЕНО
        self.current_search = ""
        
        # Создаём основной контейнер
        self.container = tk.Frame(self.parent)
        self.container.pack(fill=tk.BOTH, expand=True, pady=2)
        
        # Панель поиска (если включена)
        if searchable:
            self.search_frame = tk.Frame(self.container)
            self.search_frame.pack(fill=tk.X, pady=(0, 2))
            
            tk.Label(self.search_frame, text="🔍 Поиск:").pack(side=tk.LEFT, padx=2)
            self.search_entry = tk.Entry(self.search_frame, width=15)
            self.search_entry.pack(side=tk.LEFT, padx=2)
            self.search_entry.bind('<KeyRelease>', self._on_search_change)
            
            tk.Button(self.search_frame, text="✕", command=self.clear_search,
                     font=("Arial", 8), width=2).pack(side=tk.LEFT, padx=2)
        
        # Панель сортировки (если включена)
        if sortable:
            self.sort_frame = tk.Frame(self.container)
            self.sort_frame.pack(fill=tk.X, pady=(0, 2))
            
            tk.Button(self.sort_frame, text="⬆ По возрастанию", 
                     command=lambda: self.sort(reverse=False),
                     font=("Arial", 8)).pack(side=tk.LEFT, padx=2)
            tk.Button(self.sort_frame, text="⬇ По убыванию", 
                     command=lambda: self.sort(reverse=True),
                     font=("Arial", 8)).pack(side=tk.LEFT, padx=2)
        
        # Создаём Listbox с прокруткой
        listbox_frame = tk.Frame(self.container)
        listbox_frame.pack(fill=tk.BOTH, expand=True)
        
        self.widget = tk.Listbox(listbox_frame, height=height)
        self.scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.widget.yview)
        self.widget.configure(yscrollcommand=self.scrollbar.set)
        
        self.widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Счётчик результатов
        if searchable:
            self.result_label = tk.Label(self.search_frame, text=f"({len(self.displayed_items)})", 
                                        font=("Arial", 7))
            self.result_label.pack(side=tk.LEFT, padx=2)
        
        # Заполняем список
        self._update_display()
        
    def _on_search_change(self, event=None):
        """Обработка изменения поискового запроса"""
        search_text = self.search_entry.get().lower()
        self.current_search = search_text
        self._apply_search()
        
    def _apply_search(self):
        """Применение поиска"""
        if not self.current_search:
            self.displayed_items = self.all_items.copy()
        else:
            self.displayed_items = [
                item for item in self.all_items 
                if self.current_search in item.lower()
            ]
        self._update_display()
        
    def _update_display(self):
        """Обновление отображения списка"""
        self.widget.delete(0, tk.END)
        for item in self.displayed_items:
            self.widget.insert(tk.END, item)
        
        # Обновляем счётчик результатов
        if hasattr(self, 'result_label'):
            self.result_label.config(text=f"({len(self.displayed_items)})")
            
    def sort(self, key=None, reverse=False):
        """Сортировка элементов
        
        Args:
            key: Функция для получения ключа сортировки
            reverse (bool): Сортировка по убыванию
        """
        self.displayed_items.sort(key=key, reverse=reverse)
        self._update_display()
        
    def search(self, text):
        """Поиск элементов по тексту
        
        Args:
            text (str): Текст для поиска
        """
        self.current_search = text.lower()
        if self.searchable:
            self.search_entry.delete(0, tk.END)
            self.search_entry.insert(0, text)
        self._apply_search()
        
    def clear_search(self):
        """Сброс поиска"""
        self.current_search = ""
        if self.searchable:
            self.search_entry.delete(0, tk.END)
        self.displayed_items = self.all_items.copy()
        self._update_display()
        
    def add_item(self, item):
        """Добавить элемент в список
        
        Args:
            item (str): Новый элемент
        """
        self.all_items.append(item)
        self.clear_search()  # Обновляем отображение
        
    def add_items(self, items):
        """Добавить несколько элементов
        
        Args:
            items (list): Список новых элементов
        """
        self.all_items.extend(items)
        self.clear_search()
        
    def remove_selected(self):
        """Удалить выбранный элемент"""
        selection = self.widget.curselection()
        if selection:
            index = selection[0]
            item = self.displayed_items[index]
            # Удаляем из оригинального списка
            self.all_items.remove(item)
            # Удаляем из отображаемого
            self.displayed_items.pop(index)
            self._update_display()
            
    def get_selected(self):
        """Получить выбранный элемент
        
        Returns:
            str or None: Выбранный элемент или None
        """
        selection = self.widget.curselection()
        if selection:
            return self.displayed_items[selection[0]]
        return None
        
    def get_all_items(self):
        """Получить все элементы (оригинальный список)
        
        Returns:
            list: Все элементы
        """
        return self.all_items.copy()
        
    def get_displayed_items(self):
        """Получить отображаемые элементы (с учётом поиска)
        
        Returns:
            list: Отображаемые элементы
        """
        return self.displayed_items.copy()
        
    def clear(self):
        """Очистить список"""
        self.all_items = []
        self.displayed_items = []
        self._update_display()
        
    def hide(self):
        """Скрыть список"""
        self.container.pack_forget()
        
    def show(self):
        """Показать список"""
        self.container.pack(fill=tk.BOTH, expand=True, pady=2)