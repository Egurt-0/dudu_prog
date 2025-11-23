import collections 
from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - lista de Frutas (Contagem)
fruits = ["macaco","uva","laranja","uva","banana",
          "banana","laranja","uva","macaco","macaco","macaco","macaco","macaco",]

print(fruits)
print(Counter(fruits))# conta quantos de cada item tem EX: macaco: 6  uva: 3


# 2 - utilizando tupla nomeada
game = namedtuple("game", ['name','price','note'])
g1 = game('FIFA 15', 25.50, 9.0)
g2 = game('Elden Ring', 250, 10.0)
print(g1)
print(g2)


# 3- ordenando dicionarios
students = {'Pedro': 23, "Ana": 22, "Ronaldo": 21, "Sebastiao": 76}
a = sorted(students.items(), key = itemgetter(0))
print(a)


# 4 - utilizando um fila em ambas extremidade
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
print(delattr)# coloquei de varze aq
deq.append(90)
deq.popleft()
deq.pop

print(deq)

# o append serve para colocar algo no final da lista, mas se eu quiser colocar no comeco eu coloco appendleft