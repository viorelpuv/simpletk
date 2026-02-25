import tkinter as tk

class Menu:
    """Меню приложения
    
    Пример:
        >>> menu = Menu(app)
        >>> file_menu = menu.add_dropdown("Файл")
        >>> menu.add_item("Файл", "Открыть", lambda: app.open_file())
        >>> menu.add_separator("Файл")
        >>> menu.add_item("Файл", "Выход", app.close)
    """
    
    def __init__(self, app):
        """Инициализация меню
        
        Args:
            app: Объект приложения App
        """
        self.app = app
        self.menu_bar = tk.Menu(app.root)
        app.root.config(menu=self.menu_bar)
        self.menus = {}
        
    def add_dropdown(self, name):
        """Добавить выпадающее меню
        
        Args:
            name (str): Название меню
            
        Returns:
            tk.Menu: Объект меню
        """
        menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=name, menu=menu)
        self.menus[name] = menu
        return menu
        
    def add_item(self, menu_name, item_text, on_click=None, shortcut=None):
        """Добавить пункт в меню
        
        Args:
            menu_name (str): Название меню
            item_text (str): Текст пункта
            on_click (callable): Функция, вызываемая при выборе
            shortcut (str): Горячая клавиша
        """
        if menu_name in self.menus:
            if shortcut:
                self.menus[menu_name].add_command(label=item_text, command=on_click, accelerator=shortcut)
            else:
                self.menus[menu_name].add_command(label=item_text, command=on_click)
        
    def add_separator(self, menu_name):
        """Добавить разделитель в меню
        
        Args:
            menu_name (str): Название меню
        """
        if menu_name in self.menus:
            self.menus[menu_name].add_separator()
            
    def add_submenu(self, parent_menu, submenu_name):
        """Добавить подменю
        
        Args:
            parent_menu (str): Название родительского меню
            submenu_name (str): Название подменю
            
        Returns:
            tk.Menu: Объект подменю
        """
        if parent_menu in self.menus:
            submenu = tk.Menu(self.menus[parent_menu], tearoff=0)
            self.menus[parent_menu].add_cascade(label=submenu_name, menu=submenu)
            self.menus[submenu_name] = submenu
            return submenu