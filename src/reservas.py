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
edad = int(input("ingrese su edad"))
