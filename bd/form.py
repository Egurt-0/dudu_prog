import streamlit as st
import dadosP


# para rodar use: C:\Users\eduar\AppData\Local\Programs\Python\Python313\python.exe -m streamlit run form.py 


st.title("Egurt") # criando um titulo para aplciacao 

nome = st.text_input("Nome do filme: ") # criando um input de texto 
ano = st.number_input("Ano de lancamento do filme: ", min_value=1990, max_value=False) # criando input de numero, com valor minimo e valor maximo = False
nota = st.slider("Nota do filme:", min_value=1.0, max_value=10.0) # criando um slider, aquele que voce desliza para escoher o valor, de 1.0 a 10.0

if st.button('Adicionar'): # criando botao de Adicionar
    dadosP.insert_data(nome, ano, nota) # se ele for clicado, ele vai insert esses dados no arquivo dadosP, que adiciona no nosso banco de dados
    st.success("Filme cadastrado") # retorno para caso tenha dado certo


filmes = dadosP.get_data() # pegando os dados do bd
st.header("Lista de Filmes") # titulo 
st.table(filmes) # printa a tabela de todos os filmes no bd