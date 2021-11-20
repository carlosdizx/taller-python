def calcular_total(pago, impuesto):
    print(f'Total a pagar: {pago + pago * impuesto}')


pago = int(input("Valor del pago sin pago sin inpuesto: "))
inpuesto = float(input("Valor del inpuesto: ")) / 100
calcular_total(pago, inpuesto)
