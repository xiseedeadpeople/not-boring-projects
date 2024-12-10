import flet as ft

def login_screen(page: ft.Page):
    page.fonts = {
        "TravelingTypewriter": "fonts/TravelingTypewriter.ttf"
    }

    phone = ft.TextField(label='Номер телефона', width=300, border_radius=10, prefix_text='+7 ',
                         text_style=ft.TextStyle(color='black', size=20),
                         prefix_style=ft.TextStyle(color='black', size=20),
                         max_length=10,
                         input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9]*$", replacement_string=""))

    password = ft.TextField(label="Пароль", width=300, border_radius=10, password=True, can_reveal_password=True,
                            text_style=ft.TextStyle(color='black', size=20),
                            )


    default_users = {}
    managers = {}

    def go_to_welcome(e):

        if not phone.value:
            phone.error_text = "missing phone..."
            page.update()

        elif not password.value:
            password.error_text = "missing password..."
            page.update()

        elif password.value in managers and managers[password.value] == password.value:
            # если менеджер обнаружен
            pass

        else:
            print(f'user: +7{phone.value}, password: {password.value}')
            page.go("/user_mainscreen")

    # TODO:
    #  - паттерн ввода номера +7 (914) 538-61-23
    #  - убрать счетчик количества символов
    #  - цвет шрифта ошибки
    #  - текст ошибки должен рпопадать после ввода номера, трайни чз     def on_hover(e):
    return ft.View(
            "/",
            [
                ft.Text('Авиахуйня', size=30, color='black'),
                phone,
                password,
                ft.ElevatedButton("Login", on_click=go_to_welcome, bgcolor='#F1F1F1', width=300),
            ],
            # scroll="always",
            spacing=20,
            bgcolor='white',
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
