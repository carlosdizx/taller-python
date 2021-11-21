from math import sin, cos, tan, exp, log

funciones = {'seno': sin, 'coseno': cos, 'tangente': tan, 'exponencial': exp, 'logaritmica': log}
funcion = {}

print("Bienvenido, a continuacion se muestran las operaciones que se pueden realizar")
contador = 1
for funcion in funciones.items():
    print(f"{contador}-{funcion[0]}")
    contador += 1

eleccion = int(input("Seleccione la funcion deseada: "))
numero = int(input("Ingresa el numero entero positivo: "))

contador = 1
for funcion in funciones.items():
    if eleccion == contador:
        break
    contador += 1
print(funcion[1](numero))

print(funcion)
