
class Game:
    name = "Egurt,Esfiha,Ruy"
    yearLaunch = 0
    multiplayer = False
    note = 0

    def __init__(self, name="",yearLaunch=0, Multiplayer=0, note=0):
        self.name = name 
        self.yearLaunch = yearLaunch
        self.multiplayer = Multiplayer
        self.note = note

    def __str__(self):
        return f"Game: {self.name}"
    
game1 = Game("The legend of Zelda", 2017, False, 9.5)
game2 = Game("F1 25", 2025, True, 6.5)

print("#### DADOS DO JOGO ####")
print(f"\nNome do jogo: {game1.name}\nAno de lancamento: {game1.yearLaunch}\n")
print(f"\nNome do jogo: {game2.name}\nAno de lancamento: {game2.yearLaunch}\n")