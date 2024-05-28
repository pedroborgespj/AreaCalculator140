# 1 - bibliotecas, frameworks e referencias externas
import pytest
from area_calculator.areaCalculator import calcular_area_quadrado, calcular_area_retangulo, calcular_area_triangulo
from utils.utils import ler_csv

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

def testar_calcular_area_triangulo_negativo():
    base = -6
    altura = 8
    resultado_esperado = "Erro: Valores negativos não são permitidos."

    resultado_obtido = calcular_area_triangulo(base, altura)

    assert resultado_esperado == resultado_obtido

# Teste Baseados em Dados = Data Driven Tests (DDT) --> Massa de Teste
# Dados em uma lista

@pytest.mark.parametrize('base, resultado_esperado',
                        [
                            (3, 9),
                            (0, 0),
                            (4.2, 17.64),
                            (-2, "Erro: Valores negativos não são permitidos.")
                        ] 
                        )

def testar_calcular_area_quadrado_lista(base, resultado_esperado):

    resultado_obtido = calcular_area_quadrado(base)

    assert resultado_esperado == resultado_obtido

# Dados em um arquivo csv

@pytest.mark.parametrize('base, altura, resultado_esperado', ler_csv('./fixtures/massa_retangulo.csv'))

def testar_calcular_area_retangulo_csv(base, altura, resultado_esperado):

    resultado_obtido = calcular_area_retangulo(float(base), float(altura))

    assert float(resultado_esperado) == round(resultado_obtido, 2)
