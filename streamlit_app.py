import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Genera dati casuali
data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.random.randn(100).cumsum()
})

# Titolo dell'applicazione
st.title('Semplice Applicazione Streamlit')

# Descrizione
st.write('Questo è un semplice esempio di applicazione Streamlit che visualizza un grafico a linee.')

# Slider per filtrare i dati
min_value = st.slider('Seleziona il valore minimo di X', min_value=1, max_value=100, value=1)
max_value = st.slider('Seleziona il valore massimo di X', min_value=1, max_value=100, value=100)

# Filtra i dati
filtered_data = data[(data['x'] >= min_value) & (data['x'] <= max_value)]

# Visualizza i dati filtrati
st.line_chart(filtered_data.set_index('x'))

# Grafico con Matplotlib
fig, ax = plt.subplots()
ax.plot(filtered_data['x'], filtered_data['y'])
st.pyplot(fig)

