import time

emojis = [
    "☀️",
    "🌤️",
    "⛅",
    "🌥️",
    "🌦️",
    "🌧️",
    "⛈️",
    "🌩️",
    "⛈️",
    "🌧️",
    "☁️",
    "🌥️",
    "⛅",
    "🌤️",
]


def animate_large_emojis(emojis):
    for emoji in emojis:
        print(emoji, end="\r")
        time.sleep(
            0.5
        )  # Ajusta la duración del sleep para controlar la velocidad de la animación


# Llama a la función para iniciar la animación con emojis más grandes
animate_large_emojis(emojis)
