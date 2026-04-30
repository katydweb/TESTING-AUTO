import pytest
from app.calcprom import calcular_promedio

def test_promedio_int():
    assert calcular_promedio([4,5,9]) == 6.0

def test_promedio_dec():
    assert calcular_promedio([7.5,9.5]) == 8.5

def test_promedio_letra():
    with pytest.raises(ValueError):
        calcular_promedio([4,5,"a",9])

def test_promedio_sin_notas():
    with pytest.raises(ValueError):
        calcular_promedio([])

def test_promedio_nota_no_valida():
    with pytest.raises(ValueError):
        calcular_promedio({4,5,20,9})

