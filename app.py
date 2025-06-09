import pandas as pd
import plotly.express as px
import streamlit as st
import sys

st.header('Analisis de venta de vehiculos usados en EEUU')

vehicles_data = pd.read_csv('vehicles_us.csv')

#Primer botón

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    car_chart3 = px.histogram(vehicles_data, x="odometer", y="price", color_discrete_sequence=px.colors.qualitative.Set1) 
    car_chart3.show()

    st.plotly_chart(car_chart3, use_container_width=True)

#Segundo Botón

hist_button = st.button('Construir evolución de precios')

if hist_button:
    st.write('Creación de la gráfica con la evolución de precios promedio')
    
    car_chart = px.line(vehicles_data, x='model_year', y='price', color='condition', color_discrete_sequence=px.colors.qualitative.Set1)
    car_chart.show()

    st.plotly_chart(car_chart, use_container_width=True)

#Primer Check list

build_lineplot = st.checkbox('Construir días promedio enlistado')

if build_lineplot: 
    st.write('Creación de la gráfica de disperción con la informacion de los días promedio enlistado por tipo de vehiculo y color')
    
    car_chart2 = px.scatter(vehicles_data, x="type", y="paint_color", color='days_listed', color_continuous_scale=px.colors.sequential.Viridis)
    car_chart2.show()

    st.plotly_chart(car_chart2, use_container_width=True)
