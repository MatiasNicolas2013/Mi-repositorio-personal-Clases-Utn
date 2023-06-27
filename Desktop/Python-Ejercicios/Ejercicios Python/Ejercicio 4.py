"""
Etapas de vida
"""
edad = int(input('Ingrese su edad'))
etapa = None
if 0 <= edad < 10:
    etapa = 'La infancia es increible y bella'

elif 10 <= edad < 20:
    etapa = 'Tienes muchos cambios, y mucho que estudiar'
else:
     etapa ='Por descubrir'


print(f'Tu edad es {edad} y {etapa}')

