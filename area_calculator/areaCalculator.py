def calcular_area_quadrado(base):
    try:
        if base < 0:
            raise ValueError('Valores negativos não são permitidos.')
        return base * base
    except ValueError as e:
        return f"Erro: {e}"

def calcular_area_retangulo(base, altura):
    try:
        if base < 0 or altura < 0:
            raise ValueError('Valores negativos não são permitidos.')
        return base * altura
    except ValueError as e:
        return f"Erro: {e}"

def calcular_area_triangulo(base, altura):
    try:
        if base < 0 or altura < 0:
            raise ValueError('Valores negativos não são permitidos.')
        return (base * altura) / 2
    except ValueError as e:
        return f"Erro: {e}"