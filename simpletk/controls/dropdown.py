'''import tkinter as tk
from tkinter import ttk

class Dropdown:
    """Выпадающий список
    
    Пример:
        >>> def on_select(city):
        ...     print(f"Выбран город: {city}")
        >>> city = Dropdown(app, ["Москва", "СПб", "Казань"], on_select=on_select)
        >>> selected = city.get()
    """
    
    def __init__(self, parent, items, on_select=None, width=20):
        """Инициализация выпадающего списка
        
        Args:
            parent: Родительский элемент
            items (list): Список элементов
            on_select (callable): Функция, вызываемая при выборе
            width (int): Ширина списка
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        self.value = tk.StringVar()
        self.widget = ttk.Combobox(self.parent, textvariable=self.value,
                                   values=items, width=width)
        self.widget.pack(pady=2)
        
        if items:
            self.value.set(items[0])
            
        if on_select:
            self.widget.bind('<<ComboboxSelected>>', lambda e: on_select(self.value.get()))
            
    def get(self):
        """Получить выбранный элемент
        
        Returns:
            str: Выбранный элемент
        """
        return self.value.get()
        
    def set(self, item):
        """Установить выбранный элемент
        
        Args:
            item (str): Элемент для выбора
        """
        self.value.set(item)
        
    def add_item(self, item):
        """Добавить элемент в список
        
        Args:
            item (str): Новый элемент
        """
        current = list(self.widget['values'])
        current.append(item)
        self.widget['values'] = current
        
    def remove_item(self, item):
        """Удалить элемент из списка
        
        Args:
            item (str): Элемент для удаления
        """
        current = list(self.widget['values'])
        if item in current:
            current.remove(item)
            self.widget['values'] = current
            
    def hide(self):
        """Скрыть выпадающий список"""
        self.widget.pack_forget()
        
    def show(self):
        """Показать выпадающий список"""
        self.widget.pack(pady=2)'''

import tkinter as tk
from tkinter import ttk

class Dropdown:
    """Выпадающий список с поддержкой сортировки
    
    Пример:
        >>> city = Dropdown(app, ["Москва", "СПб", "Казань", "Астрахань"])
        >>> city.sort()  # Сортировка по алфавиту
        >>> city.sort(reverse=True)  # Сортировка по убыванию
    """
    
    def __init__(self, parent, items, on_select=None, width=20, sortable=True):
        """Инициализация выпадающего списка
        
        Args:
            parent: Родительский элемент
            items (list): Список элементов
            on_select (callable): Функция, вызываемая при выборе
            width (int): Ширина списка
            sortable (bool): Возможность сортировки
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
            
        self.items = items.copy()
        self.sortable = sortable
        self.on_select = on_select
        
        # Создаём основной контейнер
        self.container = tk.Frame(self.parent)
        self.container.pack(fill=tk.X, pady=2)
        
        # Панель сортировки (если включена)
        if sortable:
            self.sort_frame = tk.Frame(self.container)
            self.sort_frame.pack(fill=tk.X, pady=(0, 2))
            
            tk.Button(self.sort_frame, text="⬆ Сорт.", 
                     command=self.sort_ascending,
                     font=("Arial", 7), width=5).pack(side=tk.LEFT, padx=1)
            tk.Button(self.sort_frame, text="⬇ Сорт.", 
                     command=self.sort_descending,
                     font=("Arial", 7), width=5).pack(side=tk.LEFT, padx=1)
        
        # Combobox
        self.value = tk.StringVar()
        self.widget = ttk.Combobox(self.container, textvariable=self.value,
                                   values=self.items, width=width)
        self.widget.pack(fill=tk.X)
        
        if items:
            self.value.set(items[0])
            
        if on_select:
            self.widget.bind('<<ComboboxSelected>>', lambda e: on_select(self.value.get()))
            
    def sort(self, reverse=False):
        """Сортировка элементов
        
        Args:
            reverse (bool): Сортировка по убыванию
        """
        self.items.sort(reverse=reverse)
        self.widget['values'] = self.items
        
    def sort_ascending(self):
        """Сортировка по возрастанию"""
        self.sort(reverse=False)
        
    def sort_descending(self):
        """Сортировка по убыванию"""
        self.sort(reverse=True)
        
    def get(self):
        """Получить выбранный элемент
        
        Returns:
            str: Выбранный элемент
        """
        return self.value.get()
        
    def set(self, item):
        """Установить выбранный элемент
        
        Args:
            item (str): Элемент для выбора
        """
        self.value.set(item)
        
    def add_item(self, item):
        """Добавить элемент в список
        
        Args:
            item (str): Новый элемент
        """
        self.items.append(item)
        self.widget['values'] = self.items
        
    def add_items(self, items):
        """Добавить несколько элементов
        
        Args:
            items (list): Список новых элементов
        """
        self.items.extend(items)
        self.widget['values'] = self.items
        
    def remove_item(self, item):
        """Удалить элемент из списка
        
        Args:
            item (str): Элемент для удаления
        """
        if item in self.items:
            self.items.remove(item)
            self.widget['values'] = self.items
            
    def hide(self):
        """Скрыть выпадающий список"""
        self.container.pack_forget()
        
    def show(self):
        """Показать выпадающий список"""
        self.container.pack(fill=tk.X, pady=2)