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


def animate_emojis(emojis):
    for emoji in emojis:
        print(emoji, end="\r")
        time.sleep(0.5)  # Adjust the sleep duration for the desired animation speed


# Llama a la función para iniciar la animación
animate_emojis(emojis)
