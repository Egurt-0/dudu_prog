import statistics


#*******************************************************
# MEIO AUTOEXPLICATIVO, MAS SERVE PARA VER ESTATISTICAS
#******************************************************


# 1 - media
print(statistics.mean([3,5,6,10,8]))

# 2 - mediana
print(statistics.median([1,2,4,8,9]))
print(statistics.median([1,2,3,7,8,9]))

# 3 - aplicando a moda - valor que mais se repete
print(statistics.mode([2,4,5,6,8,8,8,3,4,6,9]))

# 4 - desvio padrao
"""
- Quanto mais proximo de 0 for o desvio padrao, significa que os dados
  conjuntos estao menos dispersos

"""
print(f'{statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5]):.2f}')