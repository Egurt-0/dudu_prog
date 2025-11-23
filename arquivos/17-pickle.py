import pickle

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} - {self.idade} anos - {self.cidade}"
    



clientes = [
    Cliente("Alice", 21, "Curitiba"),
    Cliente("Pedrin matador", 19, "ZN"),
    Cliente("Jaime lerner", 89, "Carandiru"),
]



# salar a lista de clientes em um arquivo pickle
with open("dados/clientes.pickle", "w+b",) as f:
    pickle.dump(clientes, f)


# carregando os dados do arquivo pickle
with open("dados/clientes.pickle", "r+b") as f:
    clientes_carregados = pickle.load(f)

for cliente in clientes_carregados:
    print(cliente)


novo_cliente = Cliente("marcos", 23, "homessexual")
clientes_carregados.append(novo_cliente)


with open("dados/clientes.pickle", "w+b") as f:
    pickle.dump(novo_cliente, f)


