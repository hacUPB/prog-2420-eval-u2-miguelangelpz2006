def simular_desintegracion_orbital(altitud_inicial, coeficiente_arrastre, altitud_minima_seguridad):
    altitud_actual = altitud_inicial
    numero_orbitas = 0
    
    print("Simulando la desintegración orbital...")
    
    while altitud_actual > altitud_minima_seguridad:
        numero_orbitas += 1
        altitud_perdida = coeficiente_arrastre * altitud_actual
        altitud_actual -= altitud_perdida
        print(f"Órbita {numero_orbitas}: Altitud actual = {altitud_actual:.4f} km, Coeficiente de arrastre = {coeficiente_arrastre:.4f}")
        
        if altitud_perdida < 0.001:
            print("El satélite se ha estabilizado en una órbita baja.")
            print(f"Altitud final = {altitud_actual:.4f} km después de {numero_orbitas} órbitas.")
            return
    
    print(f"El satélite ha reingresado en la atmósfera terrestre después de {numero_orbitas} órbitas.")

def main():
    try:
        altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en kilómetros): "))
        altitud_minima_seguridad = float(input("Ingrese la altitud mínima segura (en kilómetros): "))
        
        coeficiente_arrastre = 0.02
        
        if altitud_inicial <= 0 or coeficiente_arrastre <= 0 or altitud_minima_seguridad <= 0:
            print("Por favor, ingrese valores positivos para la altitud y el coeficiente de arrastre.")
            return
        
        simular_desintegracion_orbital(altitud_inicial, coeficiente_arrastre, altitud_minima_seguridad)
    
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número decimal válido.")

if __name__ == "__main__":
    main()
