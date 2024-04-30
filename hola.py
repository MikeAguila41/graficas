#Para crear página web
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

#Gráfica de barras
fig2, ax2 = plt.subplots()
y_pos = titanic_data['Pclass']
x_pos = titanic_data['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel('Class')
ax2.set_xlabel('Fare')
ax2.set_title('¿Cuánto pagaron las clases del Titanic?')
st.header('Gráfica de barras del titanic')
st.pyplot(fig2)

#Gráfica de dispersión
fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data['Age'], titanic_data['Fare'])
ax3.set_ylabel('Tarifa')
ax3.set_xlabel('Edad')
st.header('Gráfica de dispersión del titanic')
st.pyplot(fig3)

#Gráfica de cajas
fig4, ax4 = plt.subplots()
ax4 = titanic_data.boxplot(['Age'])
ax4.set_ylabel('Edad')
st.header('Gráfica de cajas por edad')
st.pyplot(fig4)

#Gráfica de pastel
fig5, ax5 = plt.subplots()
hist_class = np.histogram(titanic_data['Pclass'], bins = 3, range = (1, 3))[0]

labels = ['Clase 1', 'Clase 2', 'Clase 3']
colors = ['tab:blue', 'tab:red', 'tab:green']
explode = [0, 0, 0.2]
ax5.pie(hist_class, 
        labels = labels, 
        colors = colors, 
        autopct = '%.0f%%', 
        explode = explode, 
        shadow = True)
st.header('Gráfica de pastel - Clase social')
st.pyplot(fig5)
st.dataframe(hist_class) #se ven los valores de los datos
