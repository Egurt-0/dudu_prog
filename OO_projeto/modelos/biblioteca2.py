from modelos.avaliacao import Avaliacao
from modelos.itens.iten_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):                               # esse __init__ e um metodo especial para ser executado toda vez q um novo objeto for criado
        self.nome = nome 
        self._ativo = False                                 # toda vez que um objeto detro dessa classe for criado, ele vai estar desativado === outra coisa, o under line atras do atributo significa que esse atributo e privado EX: _ativo  
        self._avaliacao = []                                                   #ou seja se eu quiser alterar esse atributo diretamente eu nao consigo, nao posso apenas falar que biblioteca_cidade.ativo = True, ele nao vai funcionar, pois o atributo e privado
        self._itens = []
        Biblioteca.bibliotecas.append(self)                 # toda vez que um objeto detro dessa classe for criado, ele vai ser adicionado a lista bibliotecas ...... objeto tem que ter .self, tudo com .self é um objeto


    def __str__(self):     # 0 __str__ ajuda a converter algo de dificl compreensao para outro que seja simples para o humano enteder
        return self.nome    
    
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'nome da biblioteca'.ljust(26)} |{'Nota media'.ljust(25)}|{'Status'}")
        for biblioteca in Biblioteca.bibliotecas:                                                                      # usamos o str() ali pois o ljust nao consegue fazer espacamento com floats ent tenho que transformar aquilo em string para ele reconhecer
            print(f"{biblioteca.nome.ljust(25)} |{str(biblioteca.media_avaliacoes.ljust(25))} {biblioteca.ativo}")     #vamos entender | para cada biblioteca na calsse biblioteca dentro das bibliotecas ele vai printar o nome dela e retornar se ela esta ativa ou nao
                                                                                                                       # porque tanta biblioteca? a primeira ali "biblioteca" e so um nome para falar de todos os itens que estao dentro da classe Biblioteca e dentro da lista bibliotecas,
                                                                                                                       # (os itens ITERADOS)
    def alterna_estado(self):
        self._ativo = not self._ativo


    @property
    def ativo(self):
       return "ATIVADA" if self._ativo else "desativada"
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media

    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)


    def exibir_itens(self):
        print(f"itens da biblioteca: {self.nome}\n")
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, "isnb"):
                msg_livro = f"{i}. (Livro)--> Titulo: {item._titulo} | Autor: {item._autor} | {item._preco} | ISBN: {item.isnb}"
                print(msg_livro)
            else:
                msg_revista = f"{i}. (Revista)--> Titulo: {item._titulo} | Autor: {item._autor} | {item._preco} | Edicao: {item.edicao}"
                print(msg_revista)
 














# class Biblioteca:
#     nome = ""
#     ativo = False

#     def __str__(self):
#         return self.nome

# biblioteca_cidade = Biblioteca()
# biblioteca_cidade.nome = "Curitiba"
# biblioteca_cidade.ativo = True

# biblioteca_shopping = Biblioteca()

# bibliotecas = [biblioteca_shopping, biblioteca_cidade]

  
# print(vars(biblioteca_cidade)) # vars = acessar as informaceos em forma de dicionario, sem precisar printar cada uma
# print(vars(biblioteca_shopping))# nesse caso ele retorna vazio, pois nao tem nenhuma informacao nesse objeto

# print(bibliotecas)

# for biblioteca in bibliotecas:                  #lembra depois do for voce pode colocar qualquer coisa,
#                                                 #mas essa coisa e um nome dado para cada item que voce vai iterar
#                                                 #no loop do for in, nesse caso para cada biblioteca em bibliotecas, ou seja biblioteca_dudu biblioteca_rafaku etc, so precisa ser um item em bibliotecas e ele vai ser iterado,
#                                                 #o nome biblioteca e so para facilitar a compreensao
#     print(vars(biblioteca))