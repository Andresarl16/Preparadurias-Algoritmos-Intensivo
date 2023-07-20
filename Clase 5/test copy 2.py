import requests
import matplotlib.pyplot as plt

response = requests.get(
    "https://raw.githubusercontent.com/Andresarl16/Preparadurias-Algoritmos-Intensivo/main/Clase%205/APIs/temperature.json"
)
data = response.json()

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
