import streamlit as st
import joblib
import pandas as pd


modelo_path = './ML/modelo_entrenado.pkl'
columnas_path = './ML/columnas_entrenamiento.pkl'
# Cargar el modelo y las columnas de entrenamiento
modelo = joblib.load(modelo_path)
columnas_entrenamiento = joblib.load(columnas_path)

# Crear la interfaz de Streamlit
st.title("Predicción de Categorías de Restaurantes")

# Pedir al usuario que ingrese los datos necesarios para la predicción
state = st.selectbox("Seleccione el estado", ["New_York", "California", "Texas", "Florida"])
stars = st.number_input("Ingrese la cantidad de estrellas", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
sentimiento = st.number_input("Ingrese el valor de sentimiento", min_value=-1.0, max_value=1.0, value=0.1, step=0.1)
sentimiento_escalado = st.number_input("Ingrese el valor de sentimiento escalado", min_value=0.0, max_value=5.0, value=3.0, step=0.1)

# Realizar la predicción cuando el usuario haga clic en el botón
if st.button("Predecir"):
    # Crear un DataFrame con las características del restaurante
    input_data = pd.DataFrame({
        'state': [state],
        'stars': [stars],
        'sentimiento': [sentimiento],
        'sentimiento_escalado': [sentimiento_escalado]
    })

    # Aplicar codificación one-hot para el estado
    input_data = pd.get_dummies(input_data)

    # Asegurarse de que todas las columnas de estado estén presentes en el conjunto de datos de entrada
    # Si falta alguna columna de estado, agregarla con valor 0
    missing_cols = set(columnas_entrenamiento) - set(input_data.columns)
    for col in missing_cols:
        input_data[col] = 0

    # Reordenar las columnas para que coincidan con el orden del conjunto de entrenamiento
    input_data = input_data[columnas_entrenamiento]

    # Realizar la predicción
    predicted_category = modelo.predict(input_data)
    st.write(f"La categoría recomendada para abrir un restaurante con {stars} estrellas en {state} es: {predicted_category[0]}")
