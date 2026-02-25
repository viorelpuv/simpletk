# Примеры 

## 📋 Содержание

1. [Простое приложение](#простое-приложение)
2. [Форма регистрации](#форма-регистрации)
3. [Калькулятор](#калькулятор)
4. [Список задач](#список-задач)
5. [Таблица товаров](#таблица-товаров)
6. [Многостраничная форма](#многостраничная-форма)
7. [Поиск и сортировка](#поиск-и-сортировка)
8. [Прокручиваемый контент](#прокручиваемый-контент)
9. [Чат](#чат)
10. [Менеджер сотрудников](#менеджер-сотрудников)

---

## Простое приложение

```python
from simpletk import App, Label, Button

app = App("Моё приложение", 400, 300)
app.center()

Label(app, "Добро пожаловать в SimpleTK!", size=16, bold=True)

def click_handler():
    app.message("Привет, мир!")

Button(app, "Нажми меня", on_click=click_handler, color="lightblue")

app.run()
```

---

## Форма регистрации

```python
from simpletk import App, Label, Input, Button, Checkbox
from simpletk.containers import Vertical, Horizontal

app = App("Регистрация", 500, 400)
app.center()

Label(app, "Создание аккаунта", size=18, bold=True)

form = Vertical(app)

Label(form, "Личные данные:", bold=True)
name = Input(form, "Имя", width=30)
email = Input(form, "Email", width=30)
password = Input(form, "Пароль", width=30)
confirm = Input(form, "Подтверждение пароля", width=30)

agree = Checkbox(form, "Я согласен с условиями")
news = Checkbox(form, "Получать новости")

buttons = Horizontal(form)

def register():
    if not name.get() or not email.get() or not password.get():
        app.warning("Заполните все поля!")
    elif password.get() != confirm.get():
        app.error("Пароли не совпадают!")
    elif not agree.is_checked():
        app.warning("Необходимо согласие!")
    else:
        app.message(f"Добро пожаловать, {name.get()}!")

Button(buttons, "Регистрация", on_click=register, color="lightgreen")
Button(buttons, "Очистить", on_click=lambda: [name.clear(), email.clear(), 
                                             password.clear(), confirm.clear()], 
       color="lightcoral")

app.run()
```

---

## Калькулятор

```python
from simpletk import App, Button, Input, Label
from simpletk.containers import Grid

app = App("Калькулятор", 300, 400)
app.center()

Label(app, "Калькулятор", size=14, bold=True)
display = Input(app, "0", width=25)

grid = Grid(app, rows=4, cols=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

def button_click(value):
    current = display.get()
    if value == '=':
        try:
            result = eval(current)
            display.set(str(result))
        except:
            display.set("Ошибка")
    else:
        if current == '0':
            display.set(value)
        else:
            display.set(current + value)

for btn_text in buttons:
    Button(grid, btn_text, 
           on_click=lambda v=btn_text: button_click(v),
           color="lightgray" if btn_text.isdigit() else "lightblue")

app.run()
```

---

## Список задач

```python
from simpletk import App, ListBox, Input, Button, Label
from simpletk.containers import Horizontal

app = App("Менеджер задач", 600, 500)
app.center()

Label(app, "Мои задачи", size=18, bold=True)

tasks = [
    "Купить продукты",
    "Сделать домашнее задание",
    "Позвонить родителям",
    "Записаться к врачу",
    "Сходить в спортзал",
    "Почитать книгу"
]

task_list = ListBox(app, tasks, height=8, sortable=True, searchable=True)

add_panel = Horizontal(app)
Label(add_panel, "Новая задача:")
new_task = Input(add_panel, "Введите задачу", width=30)

def add_task():
    task = new_task.get()
    if task and task != "Введите задачу":
        task_list.add_item(task)
        new_task.clear()
        app.message(f"Задача добавлена!")

Button(add_panel, "➕ Добавить", on_click=add_task, color="lightgreen")

control_panel = Horizontal(app)

def complete_task():
    selected = task_list.get_selected()
    if selected:
        if app.question(f"Отметить задачу как выполненную?"):
            task_list.remove_selected()
            app.message("Задача выполнена!")
    else:
        app.warning("Выберите задачу")

Button(control_panel, "✅ Выполнено", on_click=complete_task, color="lightblue")
Button(control_panel, "🔄 Сброс", on_click=task_list.clear_search, color="lightcoral")

app.run()
```

---

## Таблица товаров

```python
from simpletk import App, Table, Button, Input, Label
from simpletk.containers import Horizontal
import random

app = App("Товары", 800, 600)
app.center()

Label(app, "Каталог товаров", size=18, bold=True)

columns = ["ID", "Название", "Категория", "Цена", "Количество"]
categories = ["Электроника", "Одежда", "Книги"]

data = []
for i in range(1, 21):
    data.append([
        f"{i:03d}",
        f"Товар {i}",
        random.choice(categories),
        f"{random.randint(100, 5000)} руб.",
        random.randint(1, 100)
    ])

table = Table(app, columns, data, rows_per_page=8)

add_panel = Horizontal(app)
Label(add_panel, "Название:")
name = Input(add_panel, "Название", width=12)
Label(add_panel, "Цена:")
price = Input(add_panel, "Цена", width=8)

def add_product():
    if name.get() and price.get():
        new_id = f"{len(data)+1:03d}"
        table.add_row([new_id, name.get(), "Новое", f"{price.get()} руб.", 1])
        name.clear()
        price.clear()
    else:
        app.warning("Заполните поля")

Button(add_panel, "➕ Добавить", on_click=add_product, color="lightgreen")
Button(add_panel, "Удалить", on_click=table.delete_selected, color="lightcoral")

app.run()
```

---

## Многостраничная форма

```python
from simpletk import App, Label, Input, Button, Checkbox
from simpletk.containers import Pages, Vertical

app = App("Опрос", 500, 400)
app.center()

Label(app, "Опрос пользователей", size=18, bold=True)

pages = Pages(app)

# Страница 1
page1 = pages.add_page("Шаг 1 из 2")
form1 = Vertical(page1)
Label(form1, "Личные данные:", bold=True)
name = Input(form1, "Имя")
age = Input(form1, "Возраст")

# Страница 2
page2 = pages.add_page("Шаг 2 из 2")
form2 = Vertical(page2)
Label(form2, "Интересы:", bold=True)
tech = Checkbox(form2, "Технологии")
sport = Checkbox(form2, "Спорт")
music = Checkbox(form2, "Музыка")

def finish():
    interests = []
    if tech.is_checked(): interests.append("Технологии")
    if sport.is_checked(): interests.append("Спорт")
    if music.is_checked(): interests.append("Музыка")
    
    result = f"Имя: {name.get()}\nВозраст: {age.get()}\nИнтересы: {', '.join(interests)}"
    app.message(result, "Результаты")

Button(form2, "Завершить", on_click=finish, color="lightgreen")

app.run()
```

---

## Поиск и сортировка

```python
from simpletk import App, SearchableList, Input, Button, Label
from simpletk.containers import Horizontal

app = App("Поиск", 600, 500)
app.center()

langs = [
    "Python", "JavaScript", "Java", "C++", "C#", "Ruby",
    "Swift", "Kotlin", "Go", "Rust", "PHP", "TypeScript"
]

Label(app, "Языки программирования", size=16, bold=True)
slist = SearchableList(app, langs, height=10)

search_panel = Horizontal(app)
Label(search_panel, "Поиск:")
search_input = Input(search_panel, "Введите текст", width=20)
Button(search_panel, "Найти", 
       on_click=lambda: slist.search(search_input.get()), color="lightblue")

sort_panel = Horizontal(app)
Button(sort_panel, "А→Я", on_click=slist.sort_ascending, color="lightgreen")
Button(sort_panel, "Я→А", on_click=slist.sort_descending, color="lightgreen")
Button(sort_panel, "По длине", on_click=slist.sort_by_length_asc, color="orange")
Button(sort_panel, "Сброс", on_click=slist.clear_search, color="lightcoral")

app.run()
```

---

## Прокручиваемый контент

```python
from simpletk import App, Label, Button
from simpletk.containers import ScrollableFrame, Horizontal
import random

app = App("Галерея", 600, 500)
app.center()

Label(app, "Галерея", size=18, bold=True)

scroll = ScrollableFrame(app, height=350, bg="#f0f0f0")

for i in range(1, 31):
    card = Horizontal(scroll)
    Label(card, f"Элемент #{i:02d}", bold=True)
    Label(card, f"Значение: {random.randint(100, 999)}")
    Button(card, "Просмотр", color="lightblue")

controls = Horizontal(app)
Button(controls, "⬆ Вверх", on_click=scroll.scroll_to_top, color="lightblue")
Button(controls, "⬇ Вниз", on_click=scroll.scroll_to_bottom, color="lightblue")

app.run()
```

---

## Чат

```python
from simpletk import App, Label, Input, Button
from simpletk.containers import ScrollableFrame, Horizontal
from datetime import datetime

app = App("Чат", 500, 450)
app.center()

Label(app, "Простой чат", size=16, bold=True)

chat = ScrollableFrame(app, height=300, bg="white")

input_row = Horizontal(app)
msg_input = Input(input_row, "Введите сообщение...", width=35)

def send():
    text = msg_input.get()
    if text:
        time = datetime.now().strftime("%H:%M")
        msg_row = Horizontal(chat)
        Label(msg_row, f"[{time}]", color="gray", size=8)
        Label(msg_row, text, color="blue")
        msg_input.clear()
        chat.scroll_to_bottom()

Button(input_row, "Отправить", on_click=send, color="lightgreen")
Button(app, "Очистить", on_click=chat.clear, color="lightcoral")

app.run()
```

---

## Менеджер сотрудников

```python
from simpletk import App, Table, Button, Input, Label, Dropdown
from simpletk.containers import Horizontal

app = App("Сотрудники", 800, 600)
app.center()

Label(app, "База сотрудников", size=18, bold=True)

columns = ["ID", "Имя", "Должность", "Отдел", "Зарплата"]
data = [
    ["001", "Иванов Иван", "Разработчик", "IT", "100000"],
    ["002", "Петров Петр", "Менеджер", "Продажи", "80000"],
    ["003", "Сидорова Анна", "Бухгалтер", "Финансы", "90000"],
]

table = Table(app, columns, data, rows_per_page=5)

add_panel = Horizontal(app)
Label(add_panel, "Имя:")
name = Input(add_panel, "Имя", width=12)
Label(add_panel, "Должность:")
pos = Input(add_panel, "Должность", width=12)
Label(add_panel, "Зарплата:")
sal = Input(add_panel, "Зарплата", width=8)

def add_emp():
    if name.get() and pos.get() and sal.get():
        new_id = f"{len(data)+1:03d}"
        table.add_row([new_id, name.get(), pos.get(), "Новый", sal.get()])
        name.clear(); pos.clear(); sal.clear()

Button(add_panel, "➕ Добавить", on_click=add_emp, color="lightgreen")
Button(add_panel, "Удалить", on_click=table.delete_selected, color="lightcoral")
Button(add_panel, "Инфо", on_click=lambda: app.message(f"Выбрано: {table.get_selected()}"), 
       color="lightblue")

app.run()
```
