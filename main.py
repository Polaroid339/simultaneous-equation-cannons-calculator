import flet as ft
from itertools import product


def find_combinations(total_cards, opponent_value):
    # Definition of monsters in the Extra Deck
    fusion_levels = [1, 2, 3, 4, 5]  # Levels of Fusion monsters (1 of each)
    xyz_classes = [2, 3, 4, 5, 6]  # Classes of Xyz monsters (2 of each)

    combinations = product(fusion_levels, xyz_classes)

    valid_combinations = []
    for fusion_level, xyz_class in combinations:

        combined_total = fusion_level + 2 * xyz_class
        if combined_total == total_cards:
            if fusion_level + xyz_class == opponent_value:
                valid_combinations.append((fusion_level, xyz_class))

    return valid_combinations


def main(page: ft.Page):
    page.title = "Simultaneous Equation Cannons Calculator"
    page.window.left = 400
    page.window.top = 200
    page.window.width = 600
    page.window.height = 500
    page.window.resizable = False
    page.window.maximizable = False

    def button_clicked(e):
        try:
            total_cards = int(tf1.value)
            opponent_value = int(tf2.value)

            combinations = find_combinations(total_cards, opponent_value)
            if combinations:
                result.value = "\n".join(
                    [
                        f"-Banish: 2 Xyz (Class {xyz}), Fusion (Level {fusion})\n"
                        f"-Return to Extra Deck: Xyz (Class {xyz}), Fusion (Level {
                            fusion})"
                        for fusion, xyz in combinations
                    ]
                )
            else:
                result.value = "No valid combinations found."

        except ValueError:
            result.value = "Please enter valid numeric values."

        page.update()

    title = ft.Text(
        value="Simultaneous Equation Cannons Calculator",
        color="red",
        text_align="center",
        size=25
    )
    tf1 = ft.TextField(
        label="Enter total number of cards in play",
        keyboard_type="number",
        color="blue"
    )
    tf2 = ft.TextField(
        label="Enter level/class of an opponent's monster",
        keyboard_type="number",
        color="blue"
    )
    result = ft.TextField(
        multiline=True,
        text_align="left",
        disabled=True,
        label="Valid combinations",
        color="blue",
    )

    b = ft.ElevatedButton(
        text="Click to Calculate",
        on_click=button_clicked,
        icon="check",
        height=50,
        width=300,
        elevation=3,
        style=ft.ButtonStyle(color="green")
    )

    page.add(

        ft.Column(
            [
                title,
                ft.Container(height=15),
                tf1,
                tf2,
                ft.Container(height=10),
                b,
                ft.Container(height=20),
                result
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.update()


ft.app(main)

# flet pack main.py --name "Simultaneous Equation Cannons Calculator"
