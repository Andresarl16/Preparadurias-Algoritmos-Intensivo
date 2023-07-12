import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("test")
# Crear datos utilizando NumPy y Pandas
x = np.linspace(0, 10, 150)
y = np.sin(x)

# Crear un DataFrame de Pandas
df = pd.DataFrame({"x": x, "y": y})

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Título del gráfico
ax.set_title("Gráfico de línea")

# Etiquetas de los ejes
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

# Dibujar el gráfico de línea utilizando Pandas
df.plot(x="x", y="y", ax=ax)

# Mostrar el gráfico
plt.show()
