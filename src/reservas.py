nombre = str(input("ingrese su nombre "))
apellido = str(input("ingrese su apellido"))  
while True:
    try:
        titulos = int(input("¿Se identifica usted como señor o señora? 1. para señor 2. para señora:"))

        if titulos == 1:
            titulo = "señor"
            break
        if titulos == 2: 
            titulo = "señora"
            break
        else:
            print("entrada no valida, intente nuevamente.")
    except ValueError:
        print("vuelve a intentarlo por favor. :)")
print(" Bienvenido a goku airlines", titulo, apellido)


print("Estos son los lugares disponibles que puedes visitar: 1 Bogotá, 2 Cartagena, 3 Medellin")

while True:
    try:
        ciudad = int(input("ingrese numero de la ciudad a la que se dirige"))

        if ciudad == 1:
            lugar = "Bogotá"
            break
        if ciudad == 2: 
            lugar = "Cartagena"
            break
        if ciudad == 3: 
            lugar = "Medellin"
            break
        else:
            print("entrada no valida, intente nuevamente.")
    except ValueError:
        print("vuelve a intentarlo por favor. :)")
print(f"Enhorabuena te diriges a: {lugar}" )

while True:
    try:
        inicio = int(input("Ingrese el número de la ciudad en la que inicia su viaje (1 Bogotá, 2 Cartagena, 3 Medellín): "))
        if inicio == 1:
            empieza = "Bogotá"
        elif inicio == 2: 
            empieza = "Cartagena"
        elif inicio == 3: 
            empieza = "Medellín"
        else:
            print("Entrada no válida, intente nuevamente.")
            continue 
        
        if empieza == lugar:
            print("La ciudad de origen no puede ser la misma que la ciudad de destino. Intente nuevamente.")
        else:
            print(f"Enhorabuena, te diriges a {lugar} desde {empieza}.")
            break
    except ValueError:
        print("Vuelve a intentarlo por favor. :)")

dia= str(input("ingrese el dia de la semana (lunes, martes, miercoles, jueves, viernes)")).strip().lower()
mes= str(input("Introduzca el mes: (enero, febrero, marzo, abril, mayo, junio, juilo, agosto, septiembre, octubre, noviembre, diciembre)")).strip().lower()
while True:
    try:
        fecha = int(input("Introduzca la fecha entre 1 y 30: "))
        if 1 <= fecha <= 30:
            print(f"Fecha válida:{dia}/{fecha}/{mes}/2024")
            break  
        else:
            print("Fecha no válida, ingrésela de nuevo. Debe estar entre 1 y 30.")
    except ValueError:
        print("Entrada no válida, por favor ingrese un número entero.")



if empieza == "Bogotá":
    if lugar == "Cartagena":
        print("El viaje tendrá una distancia de 657 km.")
        distancia = 657
    elif lugar == "Medellín":
        print("El viaje tendrá una distancia de 240 km.")
        distancia = 240
elif empieza == "Cartagena":
    if lugar == "Bogotá":
        print("El viaje tendrá una distancia de 657 km.")
        distancia = 657
    elif lugar == "Medellín":
        print("El viaje tendrá una distancia de 461 km.")
        distancia = 461
elif empieza == "Medellín":
    if lugar == "Bogotá":
        print("El viaje tendrá una distancia de 657 km.")
        distancia = 657
    elif lugar == "Cartagena":
        print("El viaje tendrá una distancia de 461 km.")
        distancia = 461
    

if distancia < 400:
    if dia in ("lunes", "martes", "miercoles", "jueves"):
        precio = 79900
    elif dia in ("viernes", "sabado", "domingo"):
        precio = 119900
elif distancia > 400:
    if dia in ("lunes", "martes", "miercoles", "jueves"):
        precio = 156900
    elif dia in ("viernes", "sabado", "domingo"):
        precio= 213000
