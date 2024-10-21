import streamlit as st
import json

def coleta_nomes():
    with open("projetos.json", "r") as file:
        projetos = json.load(file)
        lista = []
        for i in projetos:
            lista.append(i)
        return lista


st.sidebar.header("PROJETOS")
add_selectbox = st.sidebar.selectbox(
    'QUAL PROJETO DESEJA VER?',
    (coleta_nomes())
)

if add_selectbox in coleta_nomes():
    with open("projetos.json", "r") as file:
        projetos = json.load(file)

    st.markdown(f"# {projetos[add_selectbox]['nome']}")
    st.write(f'{projetos[add_selectbox]['descricao']}')
    for i in projetos[add_selectbox]['imagem']:
        image = st.image(i, width=projetos[add_selectbox]['tamanho'])
    file = open(f"{projetos[add_selectbox]['git']}", "r")
    st.write(file.read())
    
        

else:
    st.markdown("## ESSE PROJETO NÂO EXISTE")