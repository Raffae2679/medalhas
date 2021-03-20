import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import pickle


regressor = pickle.load( open( "mlRegressor.p", "rb" ) )
dataframe = pickle.load(open("dataset.p", "rb"))
x_train = pickle.load(open("x_train.p", "rb"))
x_test = pickle.load(open("x_test.p", "rb"))
y_train = pickle.load(open("y_train.p", "rb"))
y_test = pickle.load(open("y_test.p", "rb"))


@st.cache()

def prediction(numero):
	salario = regressor.predict([[numero]])

	return salario[0] 




st.title("Modelo de Progressão Linear")
st.write("O modelo de Progressão Linear foi treinado usando um dataset correlacionando expêriencia e salario. O modelo tem como objetivo prever qual será o salário recebido levando em conta o tempo de expêriencia.")
st.dataframe(dataframe)
st.write("Após realizarmos o treinamento do modelo, verificamos os resultados com o dataset de treino e de teste.")

fig, ax = plt.subplots()
ax.scatter(x_train, y_train, color='red')
ax.plot(x_train, regressor.predict(x_train), color='blue')
ax.title.set_text('Salary Vs Experience (Training set)')
ax.set_xlabel('Years of experience')
ax.set_ylabel('Salary')
st.pyplot(fig)

fig, ax = plt.subplots()
ax.scatter(x_test, y_test, color='red')
ax.plot(x_train, regressor.predict(x_train), color='blue')
ax.title.set_text('Salary Vs Experience (Test set)')
ax.set_xlabel('Years of experience')
ax.set_ylabel('Salary')
st.pyplot(fig)

st.write("É perceptivel a eficacia do modelo, que após seu treinamento, conseguiu prever valores de salário bem próximos dos usados no data set de teste.")

st.sidebar.subheader("Testar modelo:")

n_ex = st.sidebar.number_input('Insira o tempo de expêriencia:')

if st.sidebar.button("Predict"):
	result = prediction(n_ex) 
	st.sidebar.success(f'O salario será de R$ {result:.2f} ')