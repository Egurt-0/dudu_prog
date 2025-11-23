
class Game:
    class Game:
        name = " "
        yearLaunch = 0
        multiplayer = False
        note = 0
    
    def __init__(self, name="",yearLaunch=0, Multiplayer=0, note=0):
        self.name = name 
        self.yearLaunch = yearLaunch
        self.multiplayer = Multiplayer
        self.note = note
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
        print(f"Media do Jogo: {self.name}: {self.totalEvaluation / self.evaluators}\n")


game1 = Game("The legend of Zelda", 2017, False, 9.5)
game2 = Game("F1 25", 2025, True, 6.5)

game1.techin_seeth()
game1.evaluate(9.9)
game1.evaluate(9.5)
game1.evaluate(8.5)
game1.average()


game2.techin_seeth()
game2.evaluate(6.9)
game2.evaluate(5.7)
game2.evaluate(7.3)
game2.average() 
