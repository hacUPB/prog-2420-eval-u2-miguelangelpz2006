Analisis: en un programa llamado satelite.py se va a realizar el proyecto, el objetivo es simular la desintegracion de un satelite, sin dar muchos detalles y especificaciones a cerca de este. Consiste en que a medida que el satelite va orbitando la tierra va perdiendo gradualmente altitud debido a la fuerza de arrastre. El saltelite comienza a una altitud inicial especifica y orbita a la tierra circularmente. se le pide al usuario que desa simular esto el dato de altitud inicial, coeficiente de arrastre y altitud minima de seguridad. se utiliza un bucle para simular cada orbita y para cada orbita se hace el proceso de calcular la perdida de altitud debido al arraastre, se le resta a la altitud actual y se aumenta gradualmente el coeficiante de arrastre, el bucle se detiene cuando la perdida de altitud es 0. Por ultimo se muestra la altitud final, el numero de orbitas completadas y si el satelite reingresa a la atmosfera o no.

#Variables de entrada: Altitud inicial. Coeficiente de arrastre. Altitud minima de seguridad.

#Variables de salida: Altitud final. El número de órbitas completadas. Si reingresó o no.

# PSEUDOCODIGO:

                                                                  #inicio
    #Definir variables
        ##imprimir:"Ingrese altitud_inicial en kilometros"
        ##Leer altitud inicial
        ##imprmir: "ingrese coeficiente_de_arrastre valor decimal pequeño"
        ##Leer coeficiente_de_arrastre
        ##imprimir:"Ingrese altitud minima de seguridad en kilometros"
        
    #Bucle para simular orbita
        ##orbita =0
        ##altitud_perdida =0
        ##altitudes = []
        ##while altitud_actual > altitud_minima_seguridad
            ### Guardar la altitud actual en la lista
            ###altitud_perdida = coeficiente_arrastre * altitud_actual
            ###altitud_actual = altitud_actual - altitud_perdida
            ###coeficiente_de_arrastre = coeficiente_de_arrastre + 0.001
            ###imprimir "orbita"+"altitud_actual"km +"altitud_perdida"km
            ### if altitud_perdida < 0.01
              ####imprimir "El satelite se ha estabilizado en la orbita {orbita}"
            ###orbitas_completadas= len(altitudes)
            ###imprimir "numero de orbitas completadas orbitas_completadas " 
          
                                                                  #fin
