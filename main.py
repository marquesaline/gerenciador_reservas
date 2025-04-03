import flet as ft
from classes import Cliente, Quarto, GerenciadorDeReservas

ger = GerenciadorDeReservas()


def configurar_dados_iniciais():
    ger.adicionar_cliente(Cliente(1, "Maria", "9999-0000", "maria@email.com"))
    ger.adicionar_cliente(Cliente(2, "João", "8888-1111", "joao@email.com"))

    ger.adicionar_quarto(Quarto(101, "single", 200))
    ger.adicionar_quarto(Quarto(102, "double", 300))


def atualizar_listas(lista_quartos, lista_clientes, lista_reservas, page):
    lista_quartos.controls.clear()
    for quarto in ger.quartos:
        lista_quartos.controls.append(ft.Text(quarto.mostrar_dados()))

    lista_clientes.controls.clear()
    for cliente in ger.clientes:
        lista_clientes.controls.append(ft.Text(cliente.mostrar_dados()))

    lista_reservas.controls.clear()
    for reserva in ger.reservas:
        lista_reservas.controls.append(ft.Text(reserva.mostrar_dados()))

    page.update()


def reservar_click(e, cliente_select, quarto_select, check_in, check_out, lista_quartos, lista_clientes, lista_reservas, page):
    if cliente_select.value and quarto_select.value and check_in.value and check_out.value:
        ger.criar_reserva(
            int(cliente_select.value),
            int(quarto_select.value),
            check_in.value,
            check_out.value
        )
        atualizar_listas(lista_quartos, lista_clientes, lista_reservas, page)


def cancelar_click(e, cliente_cancelar_select, lista_quartos, lista_clientes, lista_reservas, page):
    if cliente_cancelar_select.value:
        ger.cancelar_reserva_por_cliente(int(cliente_cancelar_select.value))
        atualizar_listas(lista_quartos, lista_clientes, lista_reservas, page)


def main(page: ft.Page):
    page.title = "Sistema de Reservas"
    page.scroll = "AUTO"
    page.theme_mode = ft.ThemeMode.LIGHT

    configurar_dados_iniciais()

    titulo = ft.Text("Refúgio dos Sonhos", size=30, weight="bold")

    lista_quartos = ft.Column()
    lista_clientes = ft.Column()
    lista_reservas = ft.Column()

    cliente_select = ft.Dropdown(label="Selecione o Cliente", options=[
        ft.dropdown.Option(str(cliente.id), cliente.nome)
        for cliente in ger.clientes
    ])

    quarto_select = ft.Dropdown(label="Selecione o Quarto", options=[
        ft.dropdown.Option(str(quarto.numero), f"{quarto.numero} - {quarto.tipo}")
        for quarto in ger.quartos
    ])

    cliente_cancelar_select = ft.Dropdown(label="Cliente para Cancelar Reserva", options=[
        ft.dropdown.Option(str(cliente.id), cliente.nome)
        for cliente in ger.clientes
    ])

    check_in = ft.TextField(label="Check-in (AAAA-MM-DD)")
    check_out = ft.TextField(label="Check-out (AAAA-MM-DD)")

    btn_reservar = ft.ElevatedButton(
        "Fazer Reserva",
        on_click=lambda e: reservar_click(e, cliente_select, quarto_select, check_in, check_out, lista_quartos, lista_clientes, lista_reservas, page)
    )

    btn_cancelar = ft.ElevatedButton(
        "Cancelar Reserva",
        on_click=lambda e: cancelar_click(e, cliente_cancelar_select, lista_quartos, lista_clientes, lista_reservas, page)
    )

    btn_mostrar_reservas = ft.ElevatedButton(
        "Mostrar Reservas",
        on_click=lambda e: atualizar_listas(lista_quartos, lista_clientes, lista_reservas, page)
    )

    # Montar interface
    page.add(
        titulo,
        ft.Text("Quartos disponíveis:"),
        lista_quartos,
        ft.Text("Clientes:"),
        lista_clientes,
        ft.Text("Reservas:"),
        lista_reservas,
        btn_mostrar_reservas,
        ft.Divider(),
        ft.Text("Criar Reserva"),
        cliente_select,
        quarto_select,
        check_in,
        check_out,
        btn_reservar,
        ft.Divider(),
        ft.Text("Cancelar Reserva"),
        cliente_cancelar_select,
        btn_cancelar
    )

    atualizar_listas(lista_quartos, lista_clientes, lista_reservas, page)


ft.app(target=main)
