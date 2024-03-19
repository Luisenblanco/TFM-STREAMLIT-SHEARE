import pandas as pd
import streamlit as st

ruta_excel ="C:/Users/user/Desktop/TFM-STREAMLIT/Data/Datos_30_LIGAS.csv"

# Carga el archivo Excel y muestra las primeras filas
df = pd.read_csv(ruta_excel, encoding='latin', sep=";")

# Renombrar la columna 4510 a "Jugador"
df = df.rename(columns={"4510": "Jugador"})

with st.sidebar.expander("📊 METRICAS SELECCIONADAS"):
    # Multiselect para que el usuario seleccione las métricas
    metricas_seleccionadas = st.multiselect("SELECCIONE LAS MÉTRICAS", df.columns)
   
    # Mostrar las métricas seleccionadas
    st.write("Métricas seleccionadas:", metricas_seleccionadas)
   
with st.sidebar.expander("🥾⚽ LOS 6 JUGADORES A COMPARAR"):
    nombres_deseados = ['Cote', 'Pablo García', 'Rafel Obrador', 'Pablo Pérez', "D. van der Kust", 'S. Laquidaín']

    # Multiselect para que el usuario seleccione nombres
    nombres_seleccionados = st.multiselect("SELECCION DE JUGADORES:⚽", nombres_deseados)

# Filtrar el DataFrame por los nombres seleccionados
df_filtrado = df[df['Jugador'].isin(nombres_seleccionados)][metricas_seleccionadas]

st.title("💻TABLA COMPARATIVA :⚽🥅")
st.image("Image\\streamlit_logo.png", width=350)

# Convertir DataFrame a HTML
df_html = df_filtrado.to_html(classes=['data'], header="true", index=False)

# Estilo CSS personalizado para la tabla
estilos_css = """
    <style>
        .data {
            border-collapse: collapse;
            width: 100%;
            border: 3px solid #3366FF; /* Líneas de la tabla más gruesas */
        }
        .data th, .data td {
            border: 3px solid #3366FF; /* Líneas de las celdas más gruesas */
            padding: 10px; /* Aumenta el espacio dentro de las celdas */
            text-align: left;
            font-size: 14px;
        }
        .data th {
            background-color: #3366FF;
            color: white;
        }
        .data tr:nth-child(even) {
            background-color: #f2f2f2; /* Cambia el color de fondo de las filas pares */
        }
        /* Cambiar color de fondo de columnas específicas */
        .data tr td:nth-child(2n+1) {
            background-color: black; /* Columnas impares en negro */
            color: white; /* Texto en columnas impares en blanco */
        }
        .data tr td:nth-child(2n) {
            background-color: #d3d3d3; /* Columnas pares en gris */
        }
    </style>
"""

# Mostrar la tabla HTML con los estilos CSS
st.markdown(estilos_css + df_html, unsafe_allow_html=True)

st.image("Image\\sports.png", width=400)
