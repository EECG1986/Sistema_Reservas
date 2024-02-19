# Definir la función para la reserva de desayuno
def reservaDesayuno(nombre_cliente, numero_personas, hora_reserva):
    confirmacion_reserva = f"Reserva de desayuno confirmada para {nombre_cliente} a las {hora_reserva} para {numero_personas} personas."
    return confirmacion_reserva

# Definir la función para la reserva de comida
def reservaComida(nombre_cliente, numero_personas, hora_reserva):
    confirmacion_reserva = f"Reserva de comida confirmada para {nombre_cliente} a las {hora_reserva} para {numero_personas} personas."
    return confirmacion_reserva

# Definir la función para la reserva de cena
def reservaCena(nombre_cliente, numero_personas, hora_reserva):
    confirmacion_reserva = f"Reserva de cena confirmada para {nombre_cliente} a las {hora_reserva} para {numero_personas} personas."
    return confirmacion_reserva

# Definir la función principal para gestionar la reserva
def gestionarReserva():
    tipo_reserva = input("¿Qué tipo de reserva desea hacer? (desayuno, comida, cena): ")
    nombre_cliente = input("Ingrese su nombre: ")
    numero_personas = int(input("Ingrese el número de personas: "))
    hora_reserva = input("Ingrese la hora de la reserva: ")

    if tipo_reserva.lower() == 'desayuno':
        confirmacion = reservaDesayuno(nombre_cliente, numero_personas, hora_reserva)
    elif tipo_reserva.lower() == 'comida':
        confirmacion = reservaComida(nombre_cliente, numero_personas, hora_reserva)
    elif tipo_reserva.lower() == 'cena':
        confirmacion = reservaCena(nombre_cliente, numero_personas, hora_reserva)
    else:
        confirmacion = "Tipo de reserva inválido."

    print(confirmacion)

# Llamar a la función principal para gestionar la reserva
gestionarReserva()
