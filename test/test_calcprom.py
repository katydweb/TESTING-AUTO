from app.calcprom import calcular_promedio

def test_promedio_int():
    assert calcular_promedio([4,5,9]) == 6.0

def test_promedio_dec():
    assert calcular_promedio([7.5,9.5]) == 8.5

def test_promedio_letra():
    assert calcular_promedio([4,5,A,9]), "Error.El valor ingresado no es un número"

#def test_promedio_sin_notas():
#    assert calcular_promedio(), "La cantidad de notas a procesar debe ser mayor a 0"

#def test_promedio_nota_no_valida():
#    assert calcular_promedio(4,5,20,9), "Error. Las notas ingresadas deben estar entre 0 y 10"

