from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app  = FastAPI()


@app.get("/")
def inicio():
    return 

jogadores = {
    1:{
        "nome" : "Alef Manga",
        "idade" : 22,
        "time" : "Coritiba"
    },
    2:{ 
        "nome" : "Messi",
        "idade" : 33,
        "time": "Barcelona"
    }
}

class Jogador(BaseModel):
    nome: str
    idade: int
    time:  str



class Atualiza_jogador(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    time: Optional[str] = None


@app.get("/get-jogador/{id_jogador}")
def get_jogador(id_jogador: int):
    return jogadores[id_jogador]


@app.get("/get-jogador-time")
def get_jogador_time(time: str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]["time"] == time:
            return jogadores[jogador_id]
    return {"Dados": "Não encontrados"}



# path-parameter       get-jogador/1


# Query parameter      get-jogador/?id=1 
#get-jogador-time?time="Barcelona"



# API Metodos



@app.post("/cadastra-jogador/{id_jogador}")
def cadastra_jogador(id_jogador: int, jogador: Jogador ):
    if id_jogador in jogadores:
        return {"Erro": "Jogador ja existente"}
    jogadores[id_jogador] = jogador
    return jogadores[id_jogador]


@app.delete("/exclui-jogador/{id_jogador}")
def exlcui_jogador(id_jogador: int):
    if id_jogador not in jogadores:
        return {"Erro": "Id nao encontrado"}
    del jogadores[id_jogador]
    return {"Mensagem": "Jogador excluido"}



@app.put("/atualiza-jogador/{id_jogador}")
def atualiza_jogador(id_jogador: int, jogador: Atualiza_jogador):
    if id_jogador not in jogadores: 
        return {"Erro": "Id nao encontrado"}
    if jogador.nome != None:
        jogadores[id_jogador]["nome"] = jogador.nome
    if jogador.idade != None:
        jogadores[id_jogador]["idade"] = jogador.idade
    if jogador.time != None:
        jogadores[id_jogador]["time"] = jogador.time

    return jogadores[id_jogador]












# Para roda, se ele disser que nao encontrou o arquivo(módulo) 'api' enta use no terminal cd fundamentos
# dai ele encotrara o arquivo, pois estará procurando dentro da pasta fundamentos
# para rodar digite uvicorn api:app --reload
