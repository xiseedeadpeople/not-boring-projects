import flet as ft
import datetime


CITIES = [
    "Москва", "Санкт-Петербург", "Екатеринбург", "Новосибирск", "Краснодар", "Сочи",
    "Казань", "Владивосток", "Омск", "Челябинск", "Нижний Новгород", "Ростов-на-Дону",
    "Уфа", "Самара", "Воронеж", "Пермь", "Красноярск", "Тюмень", "Иркутск", "Саратов",
    "Кемерово", "Тольятти", "Новокузнецк", "Барнаул", "Астрахань", "Махачкала", "Рязань",
    "Тверь", "Калуга", "Ярославль", "Курск", "Тамбов", "Ставрополь", "Новороссийск",
    "Мурманск", "Тула", "Арзамас", "Сургут", "Нижневартовск", "Чита", "Бийск", "Кострома",
    "Таганрог", "Вологда", "Киров", "Мурманск", "Владикавказ", "Черкесск", "Ижевск",
    "Липецк", "Сыктывкар", "Псков", "Смоленск", "Калининград", "Ульяновск", "Томск",
    "Анапа", "Балашиха", "Калуга", "Подольск", "Набережные Челны", "Сочи", "Магнитогорск",
    "Нижний Тагил", "Саратов", "Саранск", "Северодвинск", "Владимир", "Братск", "Армавир",
    "Нижний Новгород", "Сургут", "Белгород", "Железногорск", "Уфа", "Грозный", "Норильск",
    "Подольск", "Жуковский", "Томск", "Кострома", "Гатчина", "Курган", "Калуга", "Орехово-Зуево",
    "Ярославль", "Ессентуки", "Артек", "Казань", "Волгоград", "Калуга", "Смоленск", "Челябинск",
    "Хабаровск", "Вологда", "Мурманск", "Кострома", "Екатеринбург", "Оренбург", "Челябинск",
    "Краснодар", "Иваново", "Томск", "Набережные Челны", "Сургут", "Нижневартовск", "Барнаул",
    "Новокузнецк", "Кемерово", "Воронеж", "Липецк", "Тверь", "Ростов-на-Дону", "Грозный",
    "Рязань", "Псков", "Арзамас", "Сыктывкар", "Саранск", "Нижний Новгород", "Тамбов", "Тула",
    "Ставрополь", "Иркутск", "Грозный", "Балашиха", "Екатеринбург", "Калуга", "Томск", "Ярославль",
    "Подольск", "Таганрог", "Воронеж", "Калининград", "Ульяновск", "Тула", "Кострома", "Армавир",
    "Владимир", "Челябинск", "Мурманск", "Калуга", "Подольск", "Ессентуки", "Петрозаводск",
    "Краснодар", "Казань", "Тольятти", "Томск", "Смоленск", "Псков", "Владикавказ", "Волгоград",
    "Таганрог", "Тверь", "Сочи", "Новосибирск", "Саратов", "Красноярск", "Ярославль", "Магнитогорск",
    "Барнаул", "Пермь", "Сургут", "Астрахань", "Томск", "Воронеж", "Липецк", "Челябинск", "Армавир",
    "Норильск", "Вологда", "Черкесск", "Тула", "Ижевск", "Тверь", "Таганрог", "Нижний Тагил",
    "Чита", "Тамбов", "Курск", "Смоленск", "Пермь", "Саранск", "Смоленск", "Грозный", "Жуковский",
    "Новокузнецк", "Иркутск", "Ставрополь", "Калуга", "Рязань", "Челябинск", "Владимир", "Магнитогорск",
    "Красноярск", "Саратов", "Барнаул", "Челябинск", "Воронеж", "Мурманск", "Псков", "Петрозаводск",
    "Калуга", "Рязань", "Саратов", "Набережные Челны", "Волгоград", "Ярославль", "Нижний Новгород",
    "Томск", "Краснодар", "Сургут", "Кострома", "Смоленск", "Таганрог", "Тула", "Сыктывкар", "Тольятти"
]


def main_tab(page: ft.Page):
    formatted_date = None

    def select_city(e, field, suggestions_list):
        field.value = e.control.text
        suggestions_list.controls = []
        page.update()

    def update_suggestions(e, field, suggestions_list):
        input_text = e.control.value.lower()
        filtered_cities = [city for city in CITIES if input_text in city.lower()]
        suggestions_list.controls = [ft.TextButton(text=city, on_click=lambda e: select_city(e, field, suggestions_list)) for city in filtered_cities]

        page.update()
        # validate_form()

    from_suggestions_list = ft.Row()
    from_field = ft.TextField(
        hint_text="Откуда",
        on_change=lambda e: update_suggestions(e, from_field, from_suggestions_list),
        hint_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
        text_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
        autofocus=True,
        width=300)

    to_suggestions_list = ft.Row()
    to_field = ft.TextField(
        hint_text="Куда",
        hint_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
        text_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
        on_change=lambda e: update_suggestions(e, to_field, to_suggestions_list),
        width=300)


    def handle_change(e):
        nonlocal formatted_date
        selected_date = e.control.value
        formatted_date = selected_date.strftime('%d/%m/%Y')
        date_text.value = f'{formatted_date}'
        page.update()

    today = datetime.datetime.today()
    date_text = ft.Text(f'{datetime.datetime.today().strftime('%d/%m/%Y')}', size=20,
                        color="black", font_family="SteppeRegular")

    start_fly = ft.Container(
        date_text, width=145, height=40 ,alignment=ft.alignment.bottom_center, bgcolor='white',

        on_click=lambda e: page.open(ft.DatePicker(
            first_date=datetime.datetime(year=today.year, month=today.month, day=today.day),
            last_date=datetime.datetime(year=today.year + 1, month=today.month, day=today.day),
            on_change=handle_change))
    )

    # Поле для выбора класса билета
    classes = ["Эконом", "Комфорт", "Бизнес", "Первый класс"]
    ticket_class_field = ft.Dropdown(height=40, width=145, value=classes[0], alignment=ft.alignment.center_left,
                                     border=ft.InputBorder.NONE,
                                     text_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
                                     options=[ft.dropdown.Option(cls) for cls in classes])




    search_button = ft.Container(
        ft.Text('Найти билеты', size=20, color='white', font_family='SteppeBold'),
        on_click=lambda _: print(
            f"Откуда: {from_field.value}, Куда: {to_field.value},"
            f" Дата вылета: {formatted_date if formatted_date else 'Не выбрана'}, Класс: {ticket_class_field.value}"
        ),
        width=300, height=50, border_radius=5, alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=['#fc4795', '#7c69f0'])
    )


    return ft.View(
        route='/user_mainscreen',
        bgcolor='white',

        controls=[ft.Text('Поиск авиабилетов', color='black', size=30, font_family='SteppeSemiBold'),
                  ft.Container(height=40),
                  from_field,
                  from_suggestions_list,
                  to_field,
                  to_suggestions_list,
                  ft.Row([ticket_class_field, start_fly], width=300, spacing=20, alignment=ft.alignment.center),
                  ft.Container(height=40),

                  search_button],

        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

    )

