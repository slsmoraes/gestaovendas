# Gestao de Vendas: Passo a passo
# 
# Passo 1: titulo - Sistema de Vendas
# Passo 2: Secao Cadastrar Vendas
  # Data
  # Vendedor - Ana, Bruno, Carla
  # Produto - Notebook, Fone, Celular
  # Quantidade
  # Valor
  # Botao Cadastrar Vendas
    # No Click - Adicionar a venda na tabela
# Passo 3: Secao Vendas Cadastradas
  # Tabela com as Vendas
# Passo 4: Secao Dashboard com os graficos
  # Card/Metrica - Faturamento Total
  # Grafico de Barra / Coluna - Vendas por Vendedor 
  # Grafico de Pizza - Vendas por Prouto

# Ferramentas:
  # streamlit - Cria as intterfaces
  # pandas - Base de dados
  # plotly - Graficos

# pip install streamlit pandas plotly
# streamlit run gestao_vendas.py

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de dados
tabela_vendas = pd.read_csv("vendas.csv")  

# Passo 1: titulo - Sistema de Vendas
st.write("# Sistema de Vendas")

# Passo 2: Secao Cadastrar Vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla", "Tiao"])
produto = st.sidebar.selectbox ("Produto", ["Notebook", "Fone", "Celular"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")

botao_Cadastrar = st.sidebar.button("Cadastrar Vendas")
# No Click - Adicionar a venda na tabela
if botao_Cadastrar:
    #if data or vendedor or produto or quantidade or valor:
    #    st.warning("Todos os campos devem ser preenchidos!")
    #else:       
      nova_venda = [str(data), vendedor, produto, quantidade, valor]
      ultima_linha = len(tabela_vendas) #121 linhas
      tabela_vendas.loc[ultima_linha] = nova_venda
      tabela_vendas.to_csv("vendas.csv", index=False)
      st.success("Venda cadastrada com sucesso!")

# Passo 3: Secao Vendas Cadastradas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# Passo 4: Secao Dashboard com os graficos
st.write("## Dashboard")
# Card/Metrica - Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R${faturamento}")

# Grafico de Barra / Coluna - Vendas por Vendedor 
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# Grafico de Pizza - Vendas por Prouto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2)

# Grafico de Rosca - Vendas por Prouto
grafico3 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.3)
st.plotly_chart(grafico3)