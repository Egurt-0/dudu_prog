
class Game:
    total_games = 0 # variavel de calsse para contar o numero total de jogos- isso e a memsa coisa de um contador, pq como esta no codigo, toda vez q entra uma nova instancia ele +1 no total games

    
    def __init__(self, name="",yearLaunch=0, Multiplayer=0, note=0):
        self.name = name 
        self.yearLaunch = yearLaunch
        self.multiplayer = Multiplayer
        self.note = note
        Game.total_games +=1
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f"Game: {self.name}"
    
    def techin_seeth(self):
        print("#### DADOS DO JOGO ####")
        print(f"Nome do jogo: {self.name}")   
        print(f"Ano de lancamento: {self.yearLaunch}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Nota do jogo: {self.note}")


    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1


    def average(self):
        print(f"Media do Jogo: {self.name}: {self.totalEvaluation / self.evaluators:.1f}\n")


game1 = Game("The legend of Zelda", 2017, False, 9.5)
game2 = Game("F1 25", 2025, True, 6.5)
game3 = Game("F1 24", 2024, True, 9.0)



game1.techin_seeth()
game1.evaluate(10.0)
game1.evaluate(9.9)
game1.evaluate(9.5)
game1.average()


game3.techin_seeth()
game3.evaluate(10.0)
game3.evaluate(9.5)
game3.evaluate(8.5)
game3.average()


game2.techin_seeth()
game2.evaluate(6.9)
game2.evaluate(5.7)
game2.evaluate(7.3)
game2.average() 

# exibindo o numero total de jogos
print(f"Total de Jogos na lista: {Game.total_games}")