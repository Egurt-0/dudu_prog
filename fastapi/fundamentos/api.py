from fastapi import FastAPI


app  = FastAPI()


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


@app.get("/")
def inicio():
    return jogadores



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


# Para roda, se ele disser que nao encontrou o arquivo(módulo) 'api' enta use no terminal cd fundamentos
# dai ele encotrara o arquivo, pois estará procurando denntro da pasta fundamentos
# para rodar digite uvicorn api:app --reload