class Cliente:
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def mostrar_dados(self):
        return f"{self.id} - {self.nome} | {self.telefone} | {self.email}"


class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True

    def reservar(self):
        self.disponivel = False

    def liberar(self):
        self.disponivel = True

    def mostrar_dados(self):
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} ({self.tipo}) - R${self.preco} - {status}"
        
class Reserva:
    def __init__(self, cliente, quarto, check_in, check_out):
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.ativa = True

    def cancelar(self):
        self.ativa = False
        self.quarto.liberar()

    def mostrar_dados(self):
        status = "Ativa" if self.ativa else "Cancelada"
        return f"Reserva de {self.cliente.nome} no quarto {self.quarto.numero} de {self.check_in} a {self.check_out} - {status}"


class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def criar_reserva(self, cliente_id, quarto_numero, check_in, check_out):
        cliente_encontrado = None
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                cliente_encontrado = cliente

        quarto_encontrado = None
        for quarto in self.quartos:
            if quarto.numero == quarto_numero and quarto.disponivel:
                quarto_encontrado = quarto

        if cliente_encontrado and quarto_encontrado:
            quarto_encontrado.reservar()
            nova_reserva = Reserva(cliente_encontrado, quarto_encontrado, check_in, check_out)
            self.reservas.append(nova_reserva)
            print("Reserva criada com sucesso!")
        else:
            print("Erro: cliente ou quarto não encontrado ou quarto indisponível.")

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva.mostrar_dados())

    def cancelar_reserva_por_cliente(self, cliente_id):
        for reserva in self.reservas:
            if reserva.cliente.id == cliente_id and reserva.ativa:
                reserva.cancelar()
                print("Reserva cancelada com sucesso!")
                return
        print("Reserva ativa não encontrada para esse cliente.")



