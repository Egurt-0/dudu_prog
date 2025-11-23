from modelos.biblioteca2 import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca("A bela cidade de Curitibaa")
biblioteca_shopping = Biblioteca("TU TU TU TU MAX VERSTAPPEN")

Livro1 = Livro("1984", "Gabriel bortoleto", 30.0, "053-5746")
Livro2 = Livro("189","TU TU TU TU MAX Verstappen",1000.0, "841-789")
Revista1 = Revista("National Geographic","Lewis Hamilton", 20.0, "Quinta")

biblioteca_cidade.adicionar_item(Livro1)
biblioteca_cidade.adicionar_item(Revista1)

# biblioteca_cidade.alterna_estado()

# biblioteca_cidade.receber_avaliacao("Max Verstappen", 6.6)
# biblioteca_cidade.receber_avaliacao("Gabriel Borteoleto", 9.0)

def main():
#     Biblioteca.listar_bibliotecas
    print(vars(Livro1))
    print(vars(Revista1))
    biblioteca_cidade.exibir_itens



if __name__ == "__main__":
    main()