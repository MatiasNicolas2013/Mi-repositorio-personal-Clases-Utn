"""
Ejercicio 2:
Area y longitud de un circulo
"""
import math
input('Calcular area y longitud de circunferencia')
radio = float(input('Ingrese el radio del Circulo'))
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio
print(f'El resultado del radio,es un area de {area} y una longitud de {longitud}')
