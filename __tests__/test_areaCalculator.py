# 1 - bibliotecas, frameworks e referencias externas
import pytest
from area_calculator.areaCalculator import calcular_area_quadrado, calcular_area_retangulo, calcular_area_triangulo

# 2 - Testes

def testar_calcular_area_quadrado():
    base = 4
    resultado_esperado = 16

    resultado_obtido = calcular_area_quadrado(base)

    assert resultado_esperado == resultado_obtido

def testar_calcular_area_retangulo():
    base = 5
    altura = 6
    resultado_esperado = 30

    resultado_obtido = calcular_area_retangulo(base, altura)

    assert resultado_esperado == resultado_obtido

def testar_calcular_area_triangulo():
    base = 6
    altura = 8
    resultado_esperado = 24

    resultado_obtido = calcular_area_triangulo(base, altura)

    assert resultado_esperado == resultado_obtido

