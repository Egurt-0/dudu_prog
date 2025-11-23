
class Game: # calsse mais geral
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
        print(f"Nota do jogo: {self.note}\n")


    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1


    def average(self):
        print(f"Media do Jogo: {self.name}: {self.totalEvaluation / self.evaluators:.1f}\n")

# calsse derivada ou Subcalsse mais especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, storyline="", note=0):
        super().__init__(name, yearLaunch, storyline, note)
        self.storyline = storyline

    def techin_seeth(self):
        super().techin_seeth()
        print(f"Enrredo: {self.storyline}\n")

mult_game = Game("F1 25", 2025, True, 6.8)
mult_game.techin_seeth()

sing_game = SinglePlayerGame("Legend of Zelda Breath of the Wild", 2014, "A hisotoria de Link um pequeno grande guerreiro", 10.0,)
sing_game.techin_seeth()