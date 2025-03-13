import streamlit as st
import pandas as pd
import requests

url = "https://viacep.com.br/ws/{cep}/json/"

st.title("Busca CEP")

cep = st.text_input("Busque seu cep:")

if cep != "":

    try:
        resposta =  requests.get(url.format(cep=cep))
        dados = pd.DataFrame([resposta.json()])
        st.dataframe(dados)
    except Exception as err:
        st.error("Entre com um CEP Válido.")