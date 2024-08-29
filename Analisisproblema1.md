#variables de entrada= titulo, nombre, apellido, inicio del viaje, fin del viaje, dia de la semana, mes, fecha y preferencia de asiento
#variables de salida=  asiento asignado, costo del viaje y resultado de reserva


PSEUDO CODIGO:

                                                                                          Inicio

    #Obtener información del usuario
        ##Imprimir "¿Su titulo es (Sr. o Sra.)?: "
        ##Leer título
        ##Imprimir "Introduce tu nombre: "
        ##Leer nombre
        ##Imprimir "Introduce tu apellido: "
        ##Leer apellido
        ##Imprimir "título "+"nombre"+"apellido", ¡Bienvenido Goku airlines!"

    #Seleccionar el vuelo
        ##Distancias entre ciudades
        ##Definir distancias como {("Medellín", "Bogotá"): 240, ("Medellín", "Cartagena"): 461, ("Bogotá", "Cartagena"): 657}
        ##Imprimir "Ciudades disponibles: Medellín, Bogotá, Cartagena"
        ##Imprimir "Ingresa donde inicia tu viaje (Medellín, Bogotá, Cartagena): "
        ##Leer donde inicia tu viaje
        ##Imprimir "Ingresa tu destino (Medellín, Bogotá, Cartagena): "
        ##Leer destino

        ##Si origen no está en las ciudades disponibles o destino no está en las ciudades disponibles o origen es igual a destino
            Imprimir "Origen o destino inválido."

        ##Imprimir "Ingrese el día de la semana (lunes, martes, miercoles, jueves, viernes): "
        ##Leer día_de_la_Semana
        ##Imprimir "Introduzca el mes: (enero, febrero, marzo, abril, mayo, junio, juilo, agosto, septiembre, octubre, noviembre, diciembre)"
        ##Leer Mes
        ##Imprimir "Introduzca el día del mes (1-30): "
        ##Leer díaMes

        ##Si díaMes < 1 o díaMes > 30
            Imprimir "Día del mes inválido. Debe estar entre 1 y 30."
        ##Obtener distancia
          #Si (origen, destino) está en distancias
            #Definir distancia como distancias[(origen, destino)]
          #Sino
            #Definir distancia como distancias[(destino, origen)]


        ##Determinar precio
         #Si distancia < 400
            #Si díaSemana está en ["lunes", "martes", "miércoles", "jueves"]
                #precio = 79900
            #Sino
                #precio = 119900
         #Sino
            #Si díaSemana está en ["lunes", "martes", "miércoles", "jueves"]
                #precio = 156900
            #Sino
                #precio = 213000

        #Retornar origen, destino, precio


        ##Función para asignar un asiento
            #Imprimir "¿Prefiere un asiento en el pasillo, junto a la ventana, o no tiene preferencia? (Pasillo, Ventana, Sin preferencia): "
            #Leer preferencia

        #Si preferencia es "pasillo"
            #tipoAsiento = "C"
        #SinoSi preferencia es "ventana"
            #tipoAsiento = "A"
        #Sino
            #tipoAsiento = "B"

        ## Seleccionar número de asiento aleatorio
         #Definir número asiento como número aleatorio entre 1 y 29
         #asientoAsignado = númeroAsiento + tipoAsiento

         #mostrar asientoAsignado

    ## Mostrar resultado de reserva
        Imprimir "Tu vuelo de "origen" a "destino" del "díaSemana" "díaMes" de "mes" está reservado."
        Imprimir "Precio del boleto: $" + precio
        Imprimir "Tu asiento es: " asientoAsignado



                                                                                            Fin
