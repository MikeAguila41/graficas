#Para crear página web
import streamlit as st
import pandas as pd

#creamos el titulo de la app
st.title('Mi primera app')
st.header('Demo app')
st.write('Demo de sitio con graficas')

#se imprime el archivo en la página web
titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)