import flet as ft
from flet_core import LinearGradient

# TODO:
#  https://habr.com/ru/articles/237931/                                -       DPI, screen resolution
#  https://danilin.biz/ios-device-display-resolution-reference         -       logic iphone screen resolution



def main(page: ft.Page):
    page.bgcolor = 'white'
    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable =False
    page.spacing = 0
    page.padding = 0

    def youchangechoice(e):
        """ функция, которая отвечает за выбранный таб """
        youindex = e.control.selected_index
        namescreen = e.control.tabs[youindex].text

        for i in range(0, len(e.control.tabs)):
            if youindex == i:
                # set screen name
                page.controls[0].controls[0].content.controls[0].value = namescreen

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
            ft.Tab(text='Home', icon='Home'),
            ft.Tab(text='Face', icon='face'),
            ft.Tab(text='Person', icon='person'),
            ft.Tab(text='Notifications', icon='notification_add'),
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
                    ft.Text(value='Flet App', size=25, color='white', weight=ft.FontWeight.BOLD),
                    ft.IconButton(icon='notifications', icon_size=25, icon_color='white'),
                    ft.IconButton(icon='search', icon_size=25, icon_color='white')]
                   ),
            mytab],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    page.overlay.append(mybar)
    page.add(
        ft.Column([
            ft.Container(
                margin=ft.margin.only(top=page.window.height / 2),
                alignment=ft.alignment.center,
                content=ft.Column([ft.Text('Home', size=30, color='black')])
            )
        ])
    )

ft.app(target=main)
