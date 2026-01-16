import flet

def main(page:flet.Page):
    page.title = "CAIO FERREIRA" # para definir essas bagaça de page. tem que usar o " = "
    page.bgcolor = flet.Colors.TEAL_ACCENT_400
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.vertical_alignment = flet.MainAxisAlignment.SPACE_EVENLY
    page.add(flet.Text(value="Eguroo, 4 da manha estudando flet"), flet.Container(flet.Text(value="Hoje achei uma pizada boa"), bgcolor="blue"))
    page.update()

flet.app(target=main)