def solicitar_notas():
    while True:
        cantidad_notas = input("¿Cuántas notas desea ingresar?: ")
        if cantidad_notas.isdigit() and int(cantidad_notas) > 0:
            cantidad_notas = int(cantidad_notas)
            notas = []
            for i in range(cantidad_notas):
                while True:
                    try:
                        nota = float(input("Ingresar nota: "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("Error: La nota ingresada debe ser entre 0 y 10")
                    except ValueError:
                        print("Error. El valor ingresado no es un número")
            return notas
        else:
            print("La cantidad de notas a procesar debe ser mayor a 0")


def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio
    



