import random

usuarios = [
    {"Dni": 12345678, "Nombre": "Juan Perez", "Saldo": 10000, "FacturasAdeudadas": [
        {"Servicio": "Luz", "Vencimiento": "10/09/2025", "Valor": 2500},
        {"Servicio": "Agua", "Vencimiento": "15/09/2025", "Valor": 1500}
    ]},
    {"Dni": 87654321, "Nombre": "Maria Lopez", "Saldo": 5000, "FacturasAdeudadas": [
        {"Servicio": "Gas", "Vencimiento": "12/09/2025", "Valor": 3000}
    ]}
]

sucursales = {
    "Zona Norte": ["Tigre", "San Fernando", "San Isidro"],
    "Zona Oeste": ["Morón", "Ituzaingó", "Merlo"],
    "Zona Sur": ["Lomas de Zamora", "Avellaneda", "Lanús"]
}

def buscarUsuarioPorDni(nroBuscado):
    for usuario in usuarios:
        if usuario["Dni"] == nroBuscado:
            return usuario
    return None

def consultarSaldo(usuario):
    print(f"\nEl saldo de {usuario['Nombre']} es: ${usuario['Saldo']}")

def consultarFacturas(usuario):
    print(f"\nFacturas vencidas de {usuario['Nombre']}:")
    if usuario["FacturasAdeudadas"]:
        for factura in usuario["FacturasAdeudadas"]:
            print(f"- {factura['Servicio']} | Vence: {factura['Vencimiento']} | Valor: ${factura['Valor']}")
    else:
        print("No tienes facturas vencidas.")

def pagarFacturas(usuario):
    total = sum(f["Valor"] for f in usuario["FacturasAdeudadas"])
    if total == 0:
        print("No tienes facturas pendientes de pago.")
        return
    if usuario["Saldo"] >= total:
        usuario["Saldo"] -= total
        usuario["FacturasAdeudadas"].clear()
        print(f"Facturas pagadas. Tu nuevo saldo es: ${usuario['Saldo']}")
    else:
        print(f"Saldo insuficiente. Necesitas ${total}, pero tienes ${usuario['Saldo']}")

def consultarSucursales():
    print("\nSucursales disponibles:")
    for zona, localidades in sucursales.items():
        print(f"{zona}: {', '.join(localidades)}")

def sacarTurno():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    horas = ["10:00", "11:00", "12:00", "15:00", "16:00"]
    dia = random.choice(dias)
    hora = random.choice(horas)
    print(f"Tu turno ha sido asignado para el {dia} a las {hora}.")

print("\n**¡Hola! Soy Telmo, tu asistente virtual**")

dni = int(input("Ingrese su DNI: "))
usuarioActual = buscarUsuarioPorDni(dni)

if usuarioActual:
    print(f"\n¡Bienvenido/a {usuarioActual['Nombre']}!")
    continuar = "SI"
    while continuar.upper() == "SI":
        opcion = input("""
Ingrese el número de opción que desea:

1. Consultar saldo
2. Consultar facturas de servicios vencidas
3. Pagar facturas
4. Consultar sucursales
5. Solicitar un turno
>>>>>>>>>>>>: """)

        if opcion == "1":
            consultarSaldo(usuarioActual)
        elif opcion == "2":
            consultarFacturas(usuarioActual)
        elif opcion == "3":
            pagarFacturas(usuarioActual)
        elif opcion == "4":
            consultarSucursales()
        elif opcion == "5":
            sacarTurno()
        else:
            print("Opción inválida. Intente nuevamente.")

        continuar = input("\n¿Desea continuar? (SI/NO): ")

else:
    print("Usuario no encontrado.")

print("\n**¡Gracias por utilizar el servicio de autogestión!**")
