import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

# Lendo os dados e tratando as informações no dataframe  #

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') 

df.index = names_ids.str[0] 
df['ID'] = names_ids.str[1].str[:3] 

df = df.drop('Totals')

df_summer = df[['Gold', 'Silver', 'Bronze', 'Total']]
df_winter = df[['Gold.1', 'Silver.1', 'Bronze.1', 'Total.1']]

# Fim da leitura dos dados e tratamento do data frame



 
option = st.sidebar.selectbox( 'Para qual página você deseja ir?',
('Inicio', 'olimpíadas de Verão', 'olimpíadas de Inverno', 'Dados'))
darkmode = """
<style>
body {
  background-color: rgb(24,26,27);
  color: rgb(205, 200, 194);
}
.css-1aumxhk{
	background-color: rgb(31, 33, 35)!important;
	background-image: none;
	color: rgb(205, 200, 194)!important;
}
.st-bp{
	color: rgb(232, 230, 227);
}
.st-bu{
    background-color: rgb(24, 26, 27);
}

.st-bt{
	border-bottom-color: rgb(48,52, 54);
}
.st-bs{
	border-top-color: rgb(48,52, 54);
}
.st-br{
	border-right-color: rgb(48,52, 54);
}
.st-bq{
	border-left-color: rgb(48,52, 54);
}
.st-dw, .css-145kmo2, .st-cj{
	color: #CDC8C2;
}
.css-9t20qt:hover, .css-9t20qt:active, .css-9t20qt:focus{
	background: rgb(31,33,35);
    background-image: initial;
    background-color: rgb(31, 33, 35);
}
.st-al{
    color: rgb(131, 207, 224);
}
.css-12j8tsf, .css-197q6od{
    border-color: rgb(41, 50, 68)!important;
}
.css-10r44n0, .css-1b32pqr{
	background-color: rgb(31, 33, 35);
    color: rgb(158, 150, 137);
}
path{
	color: #CDC8C2;
}
.css-1wfujj4{
	    border-top-color: rgb(41, 50, 68);
}
.css-13qyw8b{
	background-color: rgb(31,33,35);
}
</style>
"""
ativo_dm = st.sidebar.checkbox('Dark mode')
if ativo_dm:
    st.markdown(darkmode,unsafe_allow_html=True)


if option == 'Inicio':
    # Cabeçalho da Página Principal
    st.title('Análise das olimpíadas')
    st.write('Iremos analisar a quantidade de medalhas que foram recebidas durante as olimpíadas (verão e inverno), vendo quais foram os países que mais ganharam medalhas, quais menos ganharam, desvio padrão, media etc.')
    st.write('O site está dividido em 4 páginas, sendo duas de análises dos dados e a última com as informações de onde foram pego os dados aqui utilizados.')
    st.write('Decidi fazer esse projeto para testar e conhecer um pouco melhor a biblioteca Streamlit, fiquei bem entusiasmado quando vi a infinidade de coisas que poderiam ser feitas, então resolvi executar esse projeto e testar um pouco de tudo. Enfim, espero ter conseguido trazer informações com essa análise.')




elif option == 'olimpíadas de Verão':

    # Cabeçalho da Página Principal
    st.title('Medalha das olimpíadas de Verão')
    st.write('análise da quantidade de medalhas recebidas pelos paises durante as olimpíadas.')

    # Bloco dos países que mais ganharam medalhas #

    st.title('Países que mais ganharam medalhas: ')
    df_total = df_summer.sort_values(by=['Total'], ascending=False).head()
    df_total = df_total.rename(columns={'Gold': '1° Gold', 'Silver': '2° Silver', 'Bronze':'3° Bronze'})
    st.bar_chart(df_total[['1° Gold', '2° Silver', '3° Bronze']])

    for i in range(5):
        st.write(str(1+i)+"° : "+ df_total.index[i]+" com um total de "+ str(df_total['Total'].iloc[i])+" medalhas.")

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= # 

    # Bloco dos países que menos ganharam medalhas #

    st.title('Países que menos ganharam medalhas: ')
    df_total_menos = df_summer.sort_values(by=['Total'], ascending=True).head()
    df_total_menos = df_total_menos.rename(columns={'Gold': '1° Gold', 'Silver': '2° Silver', 'Bronze':'3° Bronze'})
    st.bar_chart(df_total_menos[['1° Gold', '2° Silver', '3° Bronze']])

    st.write("Liechtenstein foi o único país a ter um total de zero medalhas nas olimpíadas de verão")

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= # 

    # Bloco informações estatisticas da media e desvio padrão #

    st.title('Estatisticas a respeito média e desvio padrão:')

        ## Bloco do desvio padrão das medalhas de ouro
    st.subheader("Medalhas de Ouro:")
    st.write("A média de medalhas de ouro é "+ str(df_total['1° Gold'].mean())+ " e o desvio padrão é de "+ str(df_total['1° Gold'].std()))
    fig = df_summer['Gold'].hist()
    plt.show()
    st.pyplot()

        ## Bloco do desvio padrão das medalhas de prata
    st.subheader("Medalhas de Prata:")
    st.write("A média de medalhas de prata é "+ str(df_total['2° Silver'].mean())+ " e o desvio padrão é de "+ str(df_total['2° Silver'].std()))
    fig = df_summer['Silver'].hist()
    plt.show()
    st.pyplot()

        ## Bloco do desvio padrão das medalhas de prata
    st.subheader("Medalhas de Bronze:")
    st.write("A média de medalhas de bronze é "+ str(df_total['3° Bronze'].mean())+ " e o desvio padrão é de "+ str(df_total['3° Bronze'].std()))
    fig = df_summer['Bronze'].hist()
    plt.show()
    st.pyplot()

    st.info("Valores altos de desvio padrão indicam que os valores estão mais espalhados, mais longe da média, e valores de desvio padrão baixo indicam que os valores estão mais próximos da média. ")

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    # Bloco interativo que mostra listagem dos paises com medalhas correspondentes ao slider #

    st.title("Dataframe com os dados de medalhas dos países")
    medalhas = st.slider('Quantidade total de medalhas', 0, int(df_summer['Total'].max()), 50)
    df_medalhas_total = df_summer.sort_values(by=['Total'], ascending=False)
    df_medalhas_total = df_medalhas_total[df_medalhas_total['Total']<=medalhas]
    st.dataframe(df_medalhas_total)

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

elif option == 'olimpíadas de Inverno':

    # Cabeçalho da Página Principal
    st.title('Medalha das olimpíadas de Inverno')
    st.write('análise da quantidade de medalhas recebidas pelos paises durante as olimpíadas.')

    # Bloco dos países que mais ganharam medalhas #
    
    st.title('Países que mais ganharam medalhas: ')
    df_total = df_winter.sort_values(by=['Total.1'], ascending=False).head()
    df_total = df_total.rename(columns={'Gold.1': '1° Gold', 'Silver.1': '2° Silver', 'Bronze.1':'3° Bronze'})
    st.bar_chart(df_total[['1° Gold', '2° Silver', '3° Bronze']])

    for i in range(5):
        st.write(str(1+i)+"° : "+ df_total.index[i]+" com um total de "+ str(df_total['Total.1'].iloc[i])+" medalhas.")

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    # Bloco dos países que menos ganharam medalhas #

    st.title('Países que menos ganharam medalhas: ')
    df_total_menos = df_winter.sort_values(by=['Total.1'], ascending=True)
    df_total_menos = df_total_menos[df_total_menos['Total.1']>=1].head()
    df_total_menos = df_total_menos.rename(columns={'Gold.1': '1° Gold', 'Silver.1': '2° Silver', 'Bronze.1':'3° Bronze'})
    st.bar_chart(df_total_menos[['1° Gold', '2° Silver', '3° Bronze']])

        ### Calculando total de medalhas igual a zero dos paises nos jogos de inverno

    cont=0
    for i in range(0,len(df)): 
        if df['Total.1'].iloc[i] == 0: 
            cont+=1

    st.write("Cerca de "+str(cont)+" países obtiveram um total de zero medalhas nos jogos de inverno.")

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    # Bloco informações estatisticas da media e desvio padrão #

    st.title('Estatisticas a respeito média e desvio padrão:')

            ## Bloco do desvio padrão das medalhas de ouro
    st.subheader("Medalhas de Ouro:")
    st.write("A média de medalhas de ouro é "+ str(df_total['1° Gold'].mean())+ " e o desvio padrão é de "+ str(df_total['1° Gold'].std()))
    fig = df_winter['Gold.1'].hist()
    plt.show()
    st.pyplot()

            ## Bloco do desvio padrão das medalhas de prata
    st.subheader("Medalhas de Prata:")
    st.write("A média de medalhas de prata é "+ str(df_total['2° Silver'].mean())+ " e o desvio padrão é de "+ str(df_total['2° Silver'].std()))
    fig = df_winter['Silver.1'].hist()
    plt.show()
    st.pyplot()

            ## Bloco do desvio padrão das medalhas de bronze
    st.subheader("Medalhas de Bronze:")
    st.write("A média de medalhas de bronze é "+ str(df_total['3° Bronze'].mean())+ " e o desvio padrão é de "+ str(df_total['3° Bronze'].std()))
    fig = df_winter['Bronze.1'].hist()
    plt.show()
    st.pyplot()
    
    st.info("Valores altos de desvio padrão indicam que os valores estão mais espalhados, mais longe da média, e valores de desvio padrão baixo indicam que os valores estão mais próximos da média. ")

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    # Bloco interativo que mostra listagem dos paises com medalhas correspondentes ao slider #

    st.title("Dataframe com os dados de medalhas dos países")
    medalhas = st.slider('Quantidade total de medalhas', 0, int(df_winter['Total.1'].max()), 50)
    df_medalhas_total = df_winter.sort_values(by=['Total.1'], ascending=False)
    df_medalhas_total = df_medalhas_total[df_medalhas_total['Total.1']<=medalhas]
    st.dataframe(df_medalhas_total)

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

elif option == 'Dados':
    st.title("Fonte dos dados:")
    st.write("Os dados utilizados nessa análise foram obtidos através do wikipedia. [Clicando aqui](https://docs.streamlit.io/en/stable/api.html#display-text) você consegue acessá-los.")

    st.title("Dataframes Usados Na análise:")
    options = st.multiselect('Selecione um DataFrame', ['olimpíadas de Verão', 'olimpíadas de Inverno', 'DataFrame Completo'])

    for i in options:
        if i == "olimpíadas de Verão":
            st.subheader("Dataframe com os dados das olimpíadas de verão:")
            st.dataframe(df_summer)

        elif i == "olimpíadas de Inverno":
            st.subheader("Dataframe com os dados das olimpíadas de inverno:")
            st.dataframe(df_summer)
        
        elif i == "DataFrame Completo":
            st.subheader("Dataframe com todos os dados das olimpíadas:")
            st.dataframe(df)
