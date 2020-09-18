def conocerEdad(edad, año):
    if edad > 0:
        if año > 0:
            diferenciaAños = 2070 - año
            edadFutura = edad+ diferenciaAños
            return edadFutura
        else:
            print("Error: El año ingresado es negativo")
    else:
        print("Error: La edad ingresada es negativa")