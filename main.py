def impresion(numero):
    if numero <= 0:
        return
    if numero == 1:
        print(1)
    else:
        print(numero)
        return impresion(numero - 1)


impresion(10)
