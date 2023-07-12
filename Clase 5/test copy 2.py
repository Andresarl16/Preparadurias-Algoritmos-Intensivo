import requests
import matplotlib.pyplot as plt

""" response = requests.get("URL_DE_LA_API_RESTful") """
data = {
    "pronostico_semanal": [
        {"dia": "Lunes", "temperatura_maxima": 25},
        {"dia": "Martes", "temperatura_maxima": 28},
        {"dia": "Miércoles", "temperatura_maxima": 30},
        {"dia": "Jueves", "temperatura_maxima": 29},
        {"dia": "Viernes", "temperatura_maxima": 27},
        {"dia": "Sábado", "temperatura_maxima": 26},
        {"dia": "Domingo", "temperatura_maxima": 24},
    ]
}

# Extraer los datos relevantes
temperaturas = [dia["temperatura_maxima"] for dia in data["pronostico_semanal"]]

# Crear una lista de días de la semana para el eje x del gráfico
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear el gráfico de barras
plt.bar(dias_semana, temperaturas)

# Agregar etiquetas y título
plt.xlabel("Días de la semana")
plt.ylabel("Temperatura máxima (°C)")
plt.title("Temperatura máxima diaria durante la semana")

# Mostrar el gráfico
plt.show()
