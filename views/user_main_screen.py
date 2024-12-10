import flet as ft
from flet_core import LinearGradient

# •	Регистрация и управление клиентами, оформление туров.


# TODO:
#  https://habr.com/ru/articles/237931/                                -       DPI, screen resolution
#  https://danilin.biz/ios-device-display-resolution-reference         -       logic iphone screen resolution

def main_screen(page: ft.Page):
    cntnt = ft.Column([
        ft.ElevatedButton(),
        ft.ElevatedButton(),
        ft.ElevatedButton()
    ])

    def youchangechoice(e):
        """ функция, которая отвечает за выбранный таб """
        youindex = e.control.selected_index
        namescreen = e.control.tabs[youindex].text
        print(youindex)

        if youindex == 0:
            page.add(ft.ElevatedButton('asdasd'))

        if youindex == 1:
            page.add(ft.ElevatedButton('1223', height=500),)
        page.update()


    mytab = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        unselected_label_color='black',
        label_color='white',
        indicator_color='white',
        indicator_border_radius=30,
        divider_color='black',
        divider_height=0,
        scrollable=True,
        on_change=youchangechoice,

        tabs=[
            ft.Tab(text='Главная', icon='Home'),
            ft.Tab(text='Ближайшие рейсы', icon='face'),
            ft.Tab(text='Мои билеты', icon='person'),
            ft.Tab(text='Хз', icon='notification_add')
        ]
    )

    mybar = ft.Container(
        gradient=LinearGradient(begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right,
                                colors=['#fc4795', '#7c69f0']),

        border_radius=ft.border_radius.vertical(bottom=30),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color='#fc4795'),
        width=page.window.width,
        height=150,
        padding=10,

        content=ft.Column([
            ft.Row([ft.IconButton(icon='menu', icon_size=25, icon_color='white'),
                    ft.Text(value='Flyin', size=25, color='white', weight=ft.FontWeight.BOLD),
                    ft.IconButton(icon='notifications', icon_size=25, icon_color='white'),
                    ft.IconButton(icon='search', icon_size=25, icon_color='white')]
                   ),
            mytab],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    page.overlay.append(mybar)
    return ft.View(
        route = '/user_mainscreen',
        controls=[
            ft.Column([
                ft.Container(
                    margin=ft.margin.only(top=page.window.height / 2),
                    alignment=ft.alignment.center,
                    content=ft.Column([ft.Text('Home', size=30, color='black')])
                )
            ])
        ],
        bgcolor='#FFFFFF'
    )
