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
        print(f"Nota do jogo: {self.note}\n")

class GameStudio:
    def __init__(self,name):
        self.name = name 
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studios_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"o estudio {self.name} tem jogo aq nao parceiron\n")
        else:
            average_notes = total_notes / num_games
            print(f"AVALIACAO MEDIA DO ESTIUDIO {self.name}: {average_notes:.2f}\n")
            
game1 = Game("The legend of Zelda", 2017, False, 9.5)
game2 = Game("F1 25", 2025, True, 6.5)
game3 = Game("F1 24", 2024, True, 8.2)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)


studio.evaluate_studios_quality()

for game in studio.games:
    game.techin_seeth()