class Calculadora:
    def calcular_precio_total(self, cantidad, precio_unitario, descuento, impuesto):
        if descuento > 0:
            return cantidad * precio_unitario - (cantidad * precio_unitario * descuento / 100) + (cantidad * precio_unitario * impuesto / 100)
        else:
            return cantidad * precio_unitario + (cantidad * precio_unitario * impuesto / 100)

if __name__ == '__main__':
    calculadora = Calculadora()
    cantidad =1000
    precio_unitario=1.5
    descuento = 10
    impuesto =8

    print(f"Cantidad : {cantidad}")
    print(f"Precio unitario : {precio_unitario}")
    print(f"Descuento : {descuento}%")
    print(f"Impuesto : {impuesto}%")
    print(f"Precio Total: {calculadora.calcular_precio_total(cantidad, precio_unitario, descuento, impuesto)}")