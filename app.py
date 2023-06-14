#importação de bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import os
from functions import *
import altair as alt

#configura estruturas da página
st.set_page_config(page_title="Buscador de Preço", page_icon="🔍", layout="wide")
st.markdown('Insira o produto cosmético desejado para que o site te informe os melhores preços entre as lojas: Beauty Box, Beleza na Web, Mercado livre e Amazon')

#define a função principal do site
def main():

#define a barra lateral 
    with st.sidebar:
        st.title('Beauty Deals')
        with st.form(key='form_busca'):
#cria uma caixa de texto para o usuário digitar o produto que deseja buscar 
            query = st.text_input('Digite o produto')
            # query = tipo + ' ' + query
#cria um botão de envio para iniciar a busca
            buscar = st.form_submit_button('Buscar')
#mostra informações sobre as pessoas que desenvolveram
        st.caption('Desenvolvido por:')
        st.caption("- Anna Beatriz Veronez \n- Anna Clara Legey \n- Ana Paula Salvador \n- Nataly de Abreu")
        st.caption('Sob orientação do Prof. Matheus C. Pestana (matheus.pestana@fgv.br)')
    st.title('Buscador de preços')
#verifica se o botão foi apertado
    if buscar:
        st.header('Resultados da busca')
#mostra uma animação enquanto carrega a busca
        with st.spinner('Buscando o melhor preço...'):
#realiza a busca do produto através da função ‘buscadorGeral’ e armazena o resultado em um DataFrame
            df = buscadorGeral(query)
            st.subheader('Gráficos')
            graph1, graph2 = st.columns(2)
#cria 2 gráficos usando a biblioteca ‘altair’ e exibe eles no Streamlit
            graph1.altair_chart(histoPreco(df).properties(height=300, title='Produtos por faixa de preço'), use_container_width=True)
            graph2.altair_chart(mediaPreco(df).properties(height=300, title='Preço médio por site'), use_container_width=True)
            st.subheader('Produtos')
#mostra os produtos encontrados utilizando a função ‘showProducts’
            showProducts(df.reset_index())

#certifica se o programa está sendo executado
if __name__ == '__main__':
    main()
