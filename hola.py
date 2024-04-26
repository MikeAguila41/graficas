#Para crear página web
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#creamos el titulo de la app
st.title('Titanic app')
st.header('Titanic Graphs - App ')
st.write('Gráficas del dataset titanic')
st.write('Miguel Octavio Águila Rodríguez A01706165')

#se imprime el archivo en la página web
titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)

#histograma
fig , ax = plt.subplots()
ax.hist(titanic_data['fare'])
st.header('Histograma del Titanic')
st.pyplot(fig)

