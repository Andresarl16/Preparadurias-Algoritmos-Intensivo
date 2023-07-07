days = float(input("Introduzca una cantidad de días: "))

hours = days * 24
minutes = hours * 60
seconds = minutes * 60
milliseconds = seconds * 1000

print(f"""
    {days:.2f} días equivalen a {hours:.2f} horas
    {days:.2f} días equivalen a {minutes:.2f} minutos
    {days:.2f} días equivalen a {seconds:.2f} segundos
    {days:.2f} días equivalen a {milliseconds:.2f} milisegundos
""")
