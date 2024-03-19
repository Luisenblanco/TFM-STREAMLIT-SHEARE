#!/usr/bin/env python
# coding: utf-8

# In[ ]:

"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos de los jugadores
jugadores = ['Cote', 'Pablo Pérez', 'Rafael Obrador', 'D. van der Kust', 'S. Laquidaín']
datos = [
    [4.06, 0.18, 14.79, 2.92, 2.6, 0.27, 0.14, 4.89, 0.59, 6.67],
    [3.23, 0.06, 18.42, 3.59, 2.39, 0.36, 0.06, 5.02, 0.36, 7.71],
    [4.56, 0.24, 15.78, 3.02, 3.74, 0.86, 0.19, 4.89, 0.24, 7.24],
    [3.11, 0.1, 20.26, 4.24, 2.86, 0.44, 0.35, 6.11, 0.59, 7.98],
    [0.27, 0.0, 18.68, 5.18, 0.75, 0.0, 0.0, 5.28, 0.21, 8.17]
]

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(datos, columns=['Centros', 'Asistencias', 'Duelos', 'Pases en último tercio',
                                   'Acciones de ataque', 'Jugadas claves', 'Desmarques', 'Interceptaciones',
                                   'Pases en profundidad', 'Pases progresivos'], index=jugadores)

# Definir los nombres de los jugadores y las métricas
nombres_deseados = ['Cote', 'Pablo Pérez', 'Rafael Obrador', 'D. van der Kust', 'S. Laquidaín']
metricas_seleccionadas = ['Centros', 'Asistencias', 'Duelos', 'Pases en último tercio',
                          'Acciones de ataque', 'Jugadas claves', 'Desmarques', 'Interceptaciones',
                          'Pases en profundidad', 'Pases progresivos']

# Sidebar.expander para seleccionar jugadores
with st.sidebar.expander("🥾⚽ Seleccionar Jugadores"):
    jugadores_seleccionados = st.multiselect("Selecciona los jugadores:", nombres_deseados)

# Sidebar.expander para seleccionar métricas
with st.sidebar.expander("📊 Seleccionar Métricas"):
    metricas_seleccionadas = st.multiselect("Selecciona las métricas:", metricas_seleccionadas)

# Filtrar el DataFrame por los jugadores seleccionados
df_filtrado = df.loc[jugadores_seleccionados, metricas_seleccionadas]

# Crear el gráfico de barras no agrupadas
st.title("Gráfico de Barras de Métricas de Jugadores")
st.write("Selecciona los jugadores y las métricas en los paneles laterales para actualizar el gráfico.")

# Convertir los datos a formato numérico
df_filtrado = df_filtrado.apply(pd.to_numeric, errors='coerce')

# Eliminar filas y columnas con valores NaN
df_filtrado = df_filtrado.dropna()

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
df_filtrado.plot(kind='bar', ax=ax)

# Establecer título y etiquetas de ejes
plt.title('Métricas de Jugadores')
plt.xlabel('Jugadores')
plt.ylabel('Valor')
plt.xticks(rotation=45)

# Mostrar el gráfico de barras
st.pyplot(fig)
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de los jugadores
jugadores = ['Cote', 'Pablo Pérez', 'Rafael Obrador', 'D. van der Kust', 'S. Laquidaín']
datos = [
    [4.06, 0.18, 14.79, 2.92, 2.6, 0.27, 0.14, 4.89, 0.59, 6.67],
    [3.23, 0.06, 18.42, 3.59, 2.39, 0.36, 0.06, 5.02, 0.36, 7.71],
    [4.56, 0.24, 15.78, 3.02, 3.74, 0.86, 0.19, 4.89, 0.24, 7.24],
    [3.11, 0.1, 20.26, 4.24, 2.86, 0.44, 0.35, 6.11, 0.59, 7.98],
    [0.27, 0.0, 18.68, 5.18, 0.75, 0.0, 0.0, 5.28, 0.21, 8.17]
]

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(datos, columns=['Centros', 'Asistencias', 'Duelos', 'Pases en último tercio',
                                   'Acciones de ataque', 'Jugadas claves', 'Desmarques', 'Interceptaciones',
                                   'Pases en profundidad', 'Pases progresivos'], index=jugadores)

# Definir los nombres de los jugadores y las métricas
nombres_deseados = ['Cote', 'Pablo Pérez', 'Rafael Obrador', 'D. van der Kust', 'S. Laquidaín']
metricas_seleccionadas = ['Centros', 'Asistencias', 'Duelos', 'Pases en último tercio',
                          'Acciones de ataque', 'Jugadas claves', 'Desmarques', 'Interceptaciones',
                          'Pases en profundidad', 'Pases progresivos']

# Sidebar.expander para seleccionar jugadores
with st.sidebar.expander("🥾⚽ Seleccionar Jugadores"):
    jugadores_seleccionados = st.multiselect("Selecciona los jugadores:", nombres_deseados, default=nombres_deseados)

# Sidebar.expander para seleccionar métricas
with st.sidebar.expander("📊 Seleccionar Métricas"):
    metricas_seleccionadas = st.multiselect("Selecciona las métricas:", metricas_seleccionadas)

# Filtrar el DataFrame por los jugadores seleccionados
df_filtrado = df.loc[jugadores_seleccionados, metricas_seleccionadas]

# Crear el gráfico de barras no agrupadas
st.title("Gráfico de Barras de Métricas de Jugadores")
st.write("Selecciona los jugadores y las métricas en los paneles laterales para actualizar el gráfico.")

# Convertir los datos a formato numérico
df_filtrado = df_filtrado.apply(pd.to_numeric, errors='coerce')

# Eliminar filas y columnas con valores NaN
df_filtrado = df_filtrado.dropna()

# Establecer el estilo de seaborn
sns.set_style("dark")

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
df_filtrado.reset_index().plot(kind='bar', x='index', ax=ax)

# Establecer título y etiquetas de ejes
plt.title('Métricas de Jugadores', fontsize=16)
plt.xlabel('Jugadores', fontsize=14)
plt.ylabel('Valor', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Añadir grid
plt.grid(True, axis='y')

# Cambiar el fondo a gris claro
plt.gca().patch.set_facecolor('#626469')

# Mostrar el gráfico de barras
st.pyplot(fig)
