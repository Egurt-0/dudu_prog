from decorator import my_decorator, uppercase_decorator, split_string, decorator_dudu


# @my_decorator
# def my_functions():
#     print("Dentro da PORRA da funcao")

# my_functions()


# @uppercase_decorator # quando eu coloco esse complemento, que chamamdos de decorator,
# #ele aplica algo na funcao que esta a baixo, nesse caso esse decorator server para deixar todas as letras maiusculas
# # usando o function.upper() enfim, voce pode criar qualquer decorator e aplicar a qualquer funcao
# def text():
#     return "Hello my bro, world"

# print(text())

# @split_string
# def texto_aleatorio():
#         return "FIO da PESTE VOCE, CUZAO do CARAMBAS"


# print(texto_aleatorio())


@decorator_dudu
def exemplo():
    print("FICA DE OLHO NA MAGICA")

print(exemplo())