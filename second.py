import flet as ft
from flet import *
from data import ReturnData
from card_gen import CardGenerator


def main(page: Page):
    #    page.window_title_bar_hidden = True
    #    page.window_title_bar_buttons_hidden = True

    _main_container = Container(
        expand=True,
        margin=-10,
        gradient=RadialGradient(
            center=Alignment(0, -1.25),
            radius=1.4,
            colors=[
                "#42445f",
                "#393b52",
                "#33354a",
                "#2f3143",
                "#292b3c",
                "#222331",
                "#1a1a25",
                "#1a1b26",
                "#21222f",
                "#1d1e2a",
            ]
        ),
        padding=15,
        content=Column(
            expand=True,
            controls=[
                Row(
                    expand=True,
                    alignment='center',

                )
            ]
        )
    )

    dic = ReturnData()
    for key in dic:
        _card = CardGenerator(
            dic[key]["colors"],
            dic[key]["title"],
            dic[key]["subtitle"],
            dic[key]["price"],
            dic[key]["icon"],
            dic[key]["card_icon"],
            dic[key]["card_type"],
            dic[key]["card_number"],
        )

        _main_container.content.controls[0].controls.append(_card)

    page.add(_main_container)
    page.update()


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
