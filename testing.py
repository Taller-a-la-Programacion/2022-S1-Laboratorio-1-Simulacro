#NO MODIFICAR ESTE ARCHIVO

import Laboratorio01;
import pytest;

    
def test_division_1():
    assert Laboratorio01.division(10, 2) == 5

def test_division_2():
    assert Laboratorio01.division(0, 2) == 0

def test_division_3():
    assert Laboratorio01.division(10, 10) == 1
    
def test_division_4():
    assert isinstance(Laboratorio01.division(10, 15), str) == isinstance("Error: El divisor es mayor que el dividendo", str)
    
def test_division_5():
    assert isinstance(Laboratorio01.division(10, 0), str) == isinstance("Error: La división entre CERO no es permitido", str)
                                                                        
def test_division_6():
    assert isinstance(Laboratorio01.division(10, -5), str) == isinstance("Error: Uno de los parámetros es negativo", str)

    
def test_IVA_1():
    assert Laboratorio01.calculoIVA(1, 1000) == 1130
    
def test_IVA_2():
    assert Laboratorio01.calculoIVA(2, 1000) == 1020

def test_IVA_3():
    assert Laboratorio01.calculoIVA(3, 1000) == 1060
    
def test_IVA_4():
    assert isinstance(Laboratorio01.calculoIVA(5, 1000), str) == isinstance("Error: El valor de tipoServicio debe ser 1, 2 o 3", str)

def test_IVA_5():
    assert isinstance(Laboratorio01.calculoIVA(1, 1000.5), str) == isinstance("Error: Un parámetro no es de tipo Entero", str)

def test_IVA_6():
    assert isinstance(Laboratorio01.calculoIVA(1, -1000), str) == isinstance("Error: Uno de los parámetros es negativo", str)
    
