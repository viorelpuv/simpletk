import tkinter as tk
from tkinter import ttk

class Table:
    """Таблица с пагинацией
    
    Пример:
        >>> data = [["Товар 1", "100", "10"], ["Товар 2", "200", "5"]]
        >>> table = Table(app, ["Название", "Цена", "Кол-во"], data, rows_per_page=5)
        >>> selected = table.get_selected()
        >>> table.add_row(["Новый товар", "300", "3"])
    """
    
    def __init__(self, parent, columns, data=None, rows_per_page=5):
        """Инициализация таблицы
        
        Args:
            parent: Родительский элемент
            columns (list): Список названий колонок
            data (list): Список строк данных
            rows_per_page (int): Количество строк на странице
        """
        # Get the actual tkinter widget
        if hasattr(parent, 'frame'):
            self.parent = parent.frame
        elif hasattr(parent, 'root'):
            self.parent = parent.root
        else:
            self.parent = parent
            
        self.columns = columns
        self.all_data = data or []
        self.rows_per_page = rows_per_page
        self.current_page = 0
        
        # Main frame
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Treeview frame
        self.tree_frame = tk.Frame(self.main_frame)
        self.tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings', height=rows_per_page)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Pagination controls
        self.pagination_frame = tk.Frame(self.main_frame)
        self.pagination_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.prev_btn = tk.Button(self.pagination_frame, text="←", command=self.prev_page)
        self.prev_btn.pack(side=tk.LEFT, padx=2)
        
        self.page_label = tk.Label(self.pagination_frame, text="Страница 1")
        self.page_label.pack(side=tk.LEFT, padx=10)
        
        self.next_btn = tk.Button(self.pagination_frame, text="→", command=self.next_page)
        self.next_btn.pack(side=tk.LEFT, padx=2)
        
        # Show first page
        self._show_page(0)
        
    def _show_page(self, page_num):
        """Показать указанную страницу
        
        Args:
            page_num (int): Номер страницы
        """
        self.tree.delete(*self.tree.get_children())
        
        start = page_num * self.rows_per_page
        end = start + self.rows_per_page
        page = self.all_data[start:end]
        
        for row in page:
            self.tree.insert('', tk.END, values=row)
        
        total_pages = (len(self.all_data) + self.rows_per_page - 1) // self.rows_per_page
        if total_pages == 0:
            total_pages = 1
            
        self.page_label.config(text=f"Страница {page_num + 1} из {total_pages}")
        
        self.prev_btn.config(state=tk.NORMAL if page_num > 0 else tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL if page_num < total_pages - 1 else tk.DISABLED)
        
    def prev_page(self):
        """Перейти на предыдущую страницу"""
        if self.current_page > 0:
            self.current_page -= 1
            self._show_page(self.current_page)
            
    def next_page(self):
        """Перейти на следующую страницу"""
        total_pages = (len(self.all_data) + self.rows_per_page - 1) // self.rows_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self._show_page(self.current_page)
    
    def add_row(self, row):
        """Добавить строку в таблицу
        
        Args:
            row (list): Строка данных
        """
        self.all_data.append(row)
        self._show_page(self.current_page)
        
    def add_rows(self, rows):
        """Добавить несколько строк в таблицу
        
        Args:
            rows (list): Список строк данных
        """
        self.all_data.extend(rows)
        self._show_page(self.current_page)
        
    def clear(self):
        """Очистить таблицу"""
        self.all_data = []
        self.current_page = 0
        self._show_page(0)
        
    def get_selected(self):
        """Получить выбранную строку
        
        Returns:
            list or None: Выбранная строка или None
        """
        selection = self.tree.selection()
        if selection:
            return self.tree.item(selection[0])['values']
        return None
        
    def delete_selected(self):
        """Удалить выбранную строку"""
        selection = self.tree.selection()
        if selection:
            values = self.tree.item(selection[0])['values']
            self.all_data = [row for row in self.all_data if row != values]
            self._show_page(self.current_page)