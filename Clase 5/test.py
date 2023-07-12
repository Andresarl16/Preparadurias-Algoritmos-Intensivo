import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 8, 27, 64, 125]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Configurar los límites de los ejes
ax.set_xlim(0, 6)
ax.set_ylim(0, 130)

# Título del gráfico
ax.set_title("Gráfico de curvas")

# Etiquetas de los ejes
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

# Dibujar las curvas
ax.plot(x, y1, color='blue', label='Curva 1')
ax.plot(x, y2, color='red', label='Curva 2')

# Mostrar una leyenda con las etiquetas de las curvas
ax.legend()

# Mostrar el gráfico
plt.show()
