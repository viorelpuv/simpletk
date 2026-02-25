"""
SimpleTK - Простая библиотека для создания графических интерфейсов на Python
=============================================================================

SimpleTK предоставляет простой и интуитивный API для создания GUI приложений,
построенный поверх tkinter.

Основные возможности:
    - Простой и понятный синтаксис
    - Все базовые элементы управления
    - Контейнеры для организации интерфейса
    - Продвинутые компоненты (таблицы, прокрутка, поиск)
    - Диалоговые окна одной строкой

Пример использования:
    >>> from simpletk import App, Label, Button
    >>> app = App("Моё приложение", 400, 300)
    >>> Label(app, "Привет, мир!")
    >>> Button(app, "Нажми меня", on_click=lambda: app.message("Кнопка нажата!"))
    >>> app.run()
"""

__version__ = "1.0.0"
__author__ = "viorelpuv"
__email__ = "-"
__license__ = "MIT"
__all__ = [
    # Основные классы
    'App', 'Utils', 'Menu',
    
    # Элементы управления
    'Button', 'Label', 'Input', 'Checkbox', 'RadioGroup',
    'Dropdown', 'Slider', 'ListBox', 'SearchableList',
    
    # Контейнеры
    'Horizontal', 'Vertical', 'Grid', 'ScrollableFrame',
    'Tabs', 'Pages', 'Table',
]

from .app import App
from .menu import Menu
from .utils import Utils

from .controls import (
    Button, Label, Input, Checkbox, RadioGroup,
    Dropdown, Slider, ListBox, SearchableList
)

from .containers import (
    Horizontal, Vertical, Grid, ScrollableFrame,
    Tabs, Pages, Table
)


def __getattr__(name):
    """Помощь при опечатках в названиях классов"""
    suggestions = {
        'ListBox': ['Listbox', 'List_box', 'List-Box'],
        'SearchableList': ['Searchablelist', 'Searchable_list'],
        'ScrollableFrame': ['Scrollframe', 'Scrollable_frame'],
        'RadioGroup': ['Radiogroup', 'Radio_Group'],
    }
    
    if name in suggestions:
        alternatives = ', '.join(suggestions[name])
        raise AttributeError(
            f"Модуль 'simpletk' не имеет атрибута '{name}'. "
            f"Возможно, вы имели в виду: {alternatives}"
        )
    raise AttributeError(f"Модуль 'simpletk' не имеет атрибута '{name}'")
