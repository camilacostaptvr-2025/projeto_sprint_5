import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
scatter_button = st.button("Mostrar Gráfico de Dispersão (Preço vs Quilometragem)")

# Cabeçalho
st.header("Análise Exploratória dos Anúncios de Vendas de Carros")      

if hist_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
# criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
# exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # se o botão for clicado 
# escrever uma mensagem
    st.write("(Preço vs Quilometragem)")

# criar um gráfico de dispersão    
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Preço vs Quilometragem",
        labels={"odometer": "Quilometragem", "price": "Preço"}
    )
    st.plotly_chart(fig_scatter)