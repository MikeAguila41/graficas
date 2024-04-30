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
ax.hist(titanic_data['Fare'])
st.header('Histograma del Titanic')
st.pyplot(fig)

fig2, ax2 = plt.subplots()
y_pos = titanic_data['Pclass']
x_pos = titanic_data['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel('Class')
ax2.set_xlabel('Fare')
ax2.set_title('¿Cuánto pagaron las clases del Titanic?')
st.header('Gráfica de barras del titanic')
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data['Age'], titanic_data['Fare'])
ax3.set_ylabel('Tarifa')
ax3.set_xlabel('Edad')
st.header('Gráfica de dispersión del titanic')
st.pyplot(fig3)