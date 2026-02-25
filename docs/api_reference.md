# API simpleTk

## Содержание

1. [Базовые классы](#базовые-классы)
2. [Элементы управления](#элементы-управления)
3. [Контейнеры](#контейнеры)

---

## Базовые классы

### App - главное окно

```python
App(title="My Application", width=800, height=600)
```

| Метод | Описание | Пример |
|-------|----------|--------|
| `run()` | Запуск приложения | `app.run()` |
| `close()` | Закрыть приложение | `app.close()` |
| `set_size(w, h)` | Изменить размер | `app.set_size(1024, 768)` |
| `set_title(title)` | Изменить заголовок | `app.set_title("Новое")` |
| `center()` | Центрировать окно | `app.center()` |
| `message(text)` | Инфо-сообщение | `app.message("Готово")` |
| `question(text)` | Вопрос Да/Нет | `if app.question("Уверен?"):` |
| `warning(text)` | Предупреждение | `app.warning("Внимание")` |
| `error(text)` | Ошибка | `app.error("Ошибка")` |
| `open_file(types)` | Выбрать файл | `app.open_file([("Текст","*.txt")])` |
| `open_folder()` | Выбрать папку | `app.open_folder()` |

### Utils - утилиты

```python
Utils.center_window(window, width, height)  # Центрирование окна
```

### Menu - меню

```python
menu = Menu(app)
file_menu = menu.add_dropdown("Файл")
menu.add_item("Файл", "Открыть", on_click, "Ctrl+O")
menu.add_separator("Файл")
menu.add_submenu("Файл", "Недавние")
```

---

## Элементы управления

### Button - кнопка

```python
Button(parent, text="Кнопка", on_click=None, color="lightgray")
```

| Метод | Описание |
|-------|----------|
| `set_text(text)` | Изменить текст |
| `set_color(color)` | Изменить цвет |
| `hide()` / `show()` | Скрыть/показать |

### Label - текстовая метка

```python
Label(parent, text="Текст", size=12, bold=False, color="black")
```

| Метод | Описание |
|-------|----------|
| `set_text(text)` | Изменить текст |
| `set_color(color)` | Изменить цвет |
| `hide()` / `show()` | Скрыть/показать |

### Input - поле ввода

```python
Input(parent, placeholder="", width=30)
```

| Метод | Описание |
|-------|----------|
| `get()` | Получить текст |
| `set(text)` | Установить текст |
| `clear()` | Очистить поле |
| `hide()` / `show()` | Скрыть/показать |

### Checkbox - флажок

```python
Checkbox(parent, text="Флажок", on_change=None)
```

| Метод | Описание |
|-------|----------|
| `is_checked()` | Проверить состояние |
| `set_checked(True/False)` | Установить состояние |
| `hide()` / `show()` | Скрыть/показать |

### RadioGroup - группа радиокнопок

```python
RadioGroup(parent, options=["A", "B"], on_change=None)
```

| Метод | Описание |
|-------|----------|
| `get()` | Получить выбранное |
| `set(option)` | Выбрать опцию |
| `hide()` / `show()` | Скрыть/показать |

### Dropdown - выпадающий список

```python
Dropdown(parent, items=["A", "B"], on_select=None, width=20, sortable=True)
```

| Метод | Описание |
|-------|----------|
| `get()` | Получить выбранное |
| `set(item)` | Установить значение |
| `add_item(item)` | Добавить элемент |
| `add_items(items)` | Добавить несколько |
| `remove_item(item)` | Удалить элемент |
| `sort()` | Сортировать |
| `sort_ascending()` / `sort_descending()` | Сортировка |
| `hide()` / `show()` | Скрыть/показать |

### Slider - ползунок

```python
Slider(parent, from_=0, to=100, on_change=None)
```

| Метод | Описание |
|-------|----------|
| `get()` | Получить значение |
| `set(value)` | Установить значение |
| `hide()` / `show()` | Скрыть/показать |

### ListBox - список с поиском

```python
ListBox(parent, items=["A", "B"], height=5, sortable=True, searchable=True)
```

| Метод | Описание |
|-------|----------|
| `search(text)` | Поиск по тексту |
| `clear_search()` | Сброс поиска |
| `sort(reverse=False)` | Сортировка |
| `add_item(item)` | Добавить элемент |
| `add_items(items)` | Добавить несколько |
| `remove_selected()` | Удалить выбранное |
| `get_selected()` | Получить выбранное |
| `get_all_items()` | Все элементы |
| `clear()` | Очистить список |
| `hide()` / `show()` | Скрыть/показать |

### SearchableList - расширенный список

```python
SearchableList(parent, items=["A", "B"], height=5, show_controls=True)
```

| Метод | Описание |
|-------|----------|
| `search(text)` | Поиск по тексту |
| `search_startswith(prefix)` | Поиск по началу |
| `search_endswith(suffix)` | Поиск по концу |
| `search_by_length(min, max)` | Поиск по длине |
| `search_custom(func)` | Пользовательский поиск |
| `clear_search()` | Сброс поиска |
| `sort_ascending()` / `sort_descending()` | Сортировка |
| `sort_by_length_asc()` / `sort_by_length_desc()` | По длине |
| `sort_by(key_func, reverse)` | Своя сортировка |
| `add_item(item)` | Добавить элемент |
| `remove_selected()` | Удалить выбранное |
| `get_selected()` | Получить выбранное |

---

## Контейнеры

### Horizontal - горизонтальный ряд

```python
row = Horizontal(parent)
row.add(element)  # Добавить элемент
```

### Vertical - вертикальная колонка

```python
col = Vertical(parent)
col.add(element)  # Добавить элемент
```

### Grid - сетка

```python
grid = Grid(parent, rows=3, cols=3)
grid.add(element)  # Добавить элемент (заполняет по порядку)
```

### ScrollableFrame - прокручиваемая область

```python
scroll = ScrollableFrame(parent, width=400, height=300, bg="white")
```

| Метод | Описание |
|-------|----------|
| `add(element)` | Добавить элемент |
| `clear()` | Очистить всё |
| `scroll_to_top()` | Вверх |
| `scroll_to_bottom()` | Вниз |
| `scroll_to(fraction)` | К позиции (0-1) |
| `get_inner_frame()` | Получить внутр. фрейм |

### Tabs - вкладки

```python
tabs = Tabs(parent)
tab1 = tabs.add("Вкладка 1")  # Возвращает фрейм для размещения
```

### Pages - страницы с навигацией

```python
pages = Pages(parent)
page1 = pages.add_page("Страница 1")  # Возвращает фрейм
pages.switch_to(0)  # Переключиться на страницу
pages.prev()  # Предыдущая
pages.next()  # Следующая
```

### Table - таблица с пагинацией

```python
table = Table(parent, columns=["A", "B"], data=[["1","2"]], rows_per_page=5)
```

| Метод | Описание |
|-------|----------|
| `add_row(row)` | Добавить строку |
| `add_rows(rows)` | Добавить несколько |
| `clear()` | Очистить |
| `get_selected()` | Получить выбранную строку |
| `delete_selected()` | Удалить выбранную |
| `prev_page()` | Пред. страница |
| `next_page()` | След. страница |

---

## Быстрый импорт

```python
# Основные классы
from simpletk import App, Utils, Menu

# Элементы управления
from simpletk.controls import Button, Label, Input, Checkbox
from simpletk.controls import RadioGroup, Dropdown, Slider, ListBox, SearchableList

# Контейнеры
from simpletk.containers import Horizontal, Vertical, Grid
from simpletk.containers import ScrollableFrame, Tabs, Pages, Table
```