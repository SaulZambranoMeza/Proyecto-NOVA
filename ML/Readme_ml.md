## MODELO DE MACHINE LEARNING

# Modelo de Machine Learning para predecir el rating futuro de los nuevos negocios: 
Desarrollamos un modelo de Machine Learning que utiliza técnicas de análisis de datos para predecir el rating que los negocios obtendrán en el futuro. Proporciona una estimación precisa del rendimiento esperado de un negocio en términos de calificaciones y reseñas segun el estado en el que desee abrirse este negocio.

# Modelos evaluados
Para este caso, se evaluaron diferentes modelos (N-cluster y Regresion Lineal), quedando como la mejor opcion un modelo de arboles de desicion el cual permite crear varias submuestras del conjunto de datos y al promediarlo mejora la precision predictiva y controla el sobreajuste.

# Desarrollo del modelo
Se le realizo un analisis de los datos, uno para tener un panorama general de la cantidad promedio de estrellas por estado y el otro para validar la relacion de las variables entre si.

Luego se procedio a realizar un LaberEncoder para poder convertir todos los datos a formato numerico y poder realizar una mejor comparacion de estos, procediendo entonces a entrenar el modelo para lo cual obtenemos un primer acurracy de 0.3474, por lo que se opta por mejorar la eficiencia del modelo aplicando una reduccion del numero de combinaciones de los hiperparametros mejorando la eficiencia del modelo hasta 0.4737.

# Desarrollo de API
Para poder implementar el modelo en Streamlit se creo un API que funcione en Linea