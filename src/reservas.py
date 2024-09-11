import random
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
print(f"te diriges a: {lugar}" )

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
        print("Vuelve a intentarlo, ingresando lo indicado por favor.")




while True:
    try:
        dia = int(input("Ingrese el día de la semana ingresando el número correspondiente (1 lunes, 2 martes, 3 miércoles, 4 jueves, 5 viernes, 6 sábado, 7 domingo): "))
        
        if dia == 1:
            dia = "lunes"
        elif dia == 2:
            dia = "martes"
        elif dia == 3:
            dia = "miércoles"
        elif dia == 4:
            dia = "jueves"
        elif dia == 5:
            dia = "viernes"
        elif dia == 6:
            dia = "sábado"
        elif dia == 7:
            dia = "domingo"
        else:
            print("Entrada no válida, intente nuevamente.")
            continue
        
        print(f"El día seleccionado es {dia}.")
        break
    
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entero.")




while True:
    try:
        mes = int(input("Ingrese el mes del año ingresando el número correspondiente (1 enero, 2 febrero, 3 marzo, 4 abril, 5 mayo, 6 junio, 7 julio, 8 agosto, 9 septiembre, 10 octubre, 11 noviembre, 12 diciembre): "))
        
        if mes == 1:
            mes = "enero"
        elif mes == 2:
            mes = "febrero"
        elif mes == 3:
            mes = "marzo"
        elif mes == 4:
            mes = "abril"
        elif mes == 5:
            mes = "mayo"
        elif mes == 6:
            mes = "junio"
        elif mes == 7:
            mes = "julio"
        elif mes == 8:
            mes = "agosto"
        elif mes == 9:
            mes = "septiembre"
        elif mes == 10:
            mes = "octubre"
        elif mes == 11:
            mes = "noviembre"
        elif mes == 12:
            mes = "diciembre"
        else:
            print("Entrada no válida, intente nuevamente.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entero.")

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
        distancia = 657
    elif lugar == "Medellín":
        distancia = 240
elif empieza == "Cartagena":
    if lugar == "Bogotá":
        distancia = 657
    elif lugar == "Medellín":
        distancia = 461
elif empieza == "Medellín":
    if lugar == "Bogotá":
        distancia = 657
    elif lugar == "Cartagena":
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


    print("Seleccione su preferencia de asiento:")
    print("1. Pasillo")
    print("2. Ventana")
    print("3. Sin preferencia")
    
    try:
        preferencia = int(input("Ingrese el número correspondiente a su preferencia (1/2/3): "))
        
        if preferencia == 1:
            tipo_asiento = "C"  
        elif preferencia == 2:
            tipo_asiento = "A"  
        elif preferencia == 3:
            tipo_asiento = "B"  
        else:
            print("Entrada no válida. Por favor ingrese 1, 2 o 3.")
        numero_asiento = random.randint(1, 29)
        a = f"{numero_asiento}{tipo_asiento}"
    
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entero.")

print("¡EN GOKU AIRLINES ESTAMOS PARA SERVIRTE! tu vuelo ha sido seleccionado correctamente {titulo}{apellido}")
print(f"El viaje hacia {lugar} desde {empieza} se llevara a cabo el {dia}/{fecha}/{mes}/2024")
print(f"Tu boleto tendrá un costo de {precio} y disfrutarás del asiento {a}")
print(f"¿Estás list@ para viajar {distancia}km con nosotros?")
