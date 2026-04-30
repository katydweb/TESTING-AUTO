from calcprom import solicitar_notas, calcular_promedio

def main():
    print("***Cálculo de Promedio Académico***")
    notas = solicitar_notas()
    promedio = calcular_promedio(notas)
    print("Promedio: ", promedio)

main()