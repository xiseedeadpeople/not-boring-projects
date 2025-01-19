import flet as ft
from flet_core.border_radius import vertical
import re


def login_screen(page: ft.Page):
    page.fonts = {
        "SteppeBlack": "fonts/Steppe-Black.ttf",
        "SteppeExtraBold": "fonts/Steppe-ExtraBold.ttf",
        "SteppeBold": "fonts/Steppe-Bold.ttf",
        "SteppeSemiBold": "fonts/Steppe-SemiBold.ttf",
        "SteppeMedium": "fonts/Steppe-Medium.ttf",
        "SteppeRegular": "fonts/Steppe-Regular.ttf",
        "SteppeBook": "fonts/Steppe-Book.ttf",
        "SteppeLight": "fonts/Steppe-Light.ttf",
        "SteppeThin": "fonts/Steppe-Thin.ttf",
    }

    def password_focus(e):
        password.error_text = ''
        page.update()

    def password_blur(e):
        if  len(password.value) == 0:
            password.error_text = 'Введите пароль'
        elif 1 <= len(password.value) < 8:
            password.error_text = 'Слишком короткий!'

        elif not re.search(r'[0-9]', password.value):
            password.error_text = 'В пароле должна быть цифра!'
        elif not re.search(r'[A-Z]', password.value):
            password.error_text = 'А заглавная буква?'
        elif not re.search(r'[a-z]', password.value):
            password.error_text = 'А маленькая буква?'
        elif not re.search(r'[.@#$%/^&+=?!,]', password.value):
            password.error_text = 'А спец. символ? (.@#$%/^&+=?!,)'

        page.update()

    def phone_focus(e):
        phone.error_text = ''
        page.update()

    def phone_blur(e):
        if  len(phone.value) == 0:
            phone.error_text = 'Введите номер'

        elif 1 <= len(phone.value) < 14:
            phone.error_text = 'Неверный формат номера'
        page.update()

    def format_phone(e):
        phone.error_text = ''
        new_value = (phone.value.replace(" ", "").replace("(", "")
                     .replace(")", "").replace("-", ""))

        if len(new_value) > 14:
            new_value = new_value[:14]


        formatted_value = ""
        if len(new_value) >= 1:
            formatted_value += f"({new_value[:3]})"
        if len(new_value) >= 4:
            formatted_value += f" {new_value[3:6]}"
        if len(new_value) >= 7:
            formatted_value += f"-{new_value[6:8]}"
        if len(new_value) >= 9:
            formatted_value += f"-{new_value[8:11]}"

        phone.value = formatted_value
        page.update()

    phone = ft.TextField(
        label='Номер телефона',
        width=300,
        border_radius=10,
        prefix_text='+7 ',
        label_style=ft.TextStyle(color='black', size=20, font_family='SteppeThin'),
        text_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
        prefix_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
        error_style=ft.TextStyle(color='red', size=15, font_family='SteppeSemiBold'),
        adaptive=True,
        border=ft.InputBorder.NONE,
        fill_color='#F9F9F9',
        input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9()\- ]*$", replacement_string=""),
        on_change=format_phone,
        on_blur=phone_blur, on_focus=phone_focus
    )

    password = ft.TextField(label="Пароль", width=300, border_radius=10, password=True, can_reveal_password=True,
                            label_style=ft.TextStyle(color='black', size=20, font_family='SteppeThin'),
                            text_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
                            prefix_style=ft.TextStyle(color='black', size=20, font_family='SteppeRegular'),
                            error_style=ft.TextStyle(color='red', size=15, font_family='SteppeSemiBold'),
                            on_focus=password_focus, on_blur=password_blur,
                            border=ft.InputBorder.NONE, fill_color='#F9F9F9', adaptive=True,
                            )

    mybarx = ft.Container(
        gradient=ft.LinearGradient(begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right,
                                colors=['#fc4795', '#7c69f0']),

        border_radius=ft.border_radius.vertical(bottom=30),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color='#fc4795'),
        width=page.window.width,height=150, alignment=ft.alignment.center,
        content=ft.Container(ft.Text('"9/11" AVIALINES', size=35, color='white', font_family='SteppeBlack'))
    )



    default_users = {}
    managers = {'1': '1'}

    def go_to_welcome(e):

        # phone
        if  len(phone.value) == 0:
            phone.error_text = 'Введите номер'
        elif 1 <= len(phone.value) < 14:
            phone.error_text = 'Неверный формат номера'

        # password
        if len(password.value) == 0:
            password.error_text = 'Введите пароль'
        elif 1 <= len(password.value) < 8:
            password.error_text = 'Слишком короткий!'
        elif not re.search(r'[0-9]', password.value):
            password.error_text = 'В пароле должна быть цифра!'
        elif not re.search(r'[A-Z]', password.value):
            password.error_text = 'А заглавная буква?'
        elif not re.search(r'[a-z]', password.value):
            password.error_text = 'А маленькая буква?'
        elif not re.search(r'[.@#$%/^&+=?!,]', password.value):
            password.error_text = 'А спец. символ? (.@#$%/^&+=?!,)'

        else:
            print(f'user: +7{phone.value.replace('(', '').replace(')', '')
                  .replace('-', '').replace(' ', '')}'),
            print(f'password: {password.value}')
            page.go("/user_mainscreen")

    btn = ft.Container(
                    ft.Text('ВОЙТИ', size=20, color='white', font_family='SteppeSemiBold'),
                    width=300, height=50, on_click=go_to_welcome, border_radius=20, alignment=ft.alignment.center,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=['#fc4795', '#7c69f0'])
                )

    return ft.View(
            "/",
            [
                mybarx, ft.Container(height=100),
                ft.Column([phone, password, btn], spacing=30)
            ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        padding=0,
        bgcolor='white')
