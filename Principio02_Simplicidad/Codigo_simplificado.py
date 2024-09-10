class Calculadora:
    def calcular_precio_total(self, cantidad, precio_unitario, descuento, impuesto):
        precio_sin_descuento = cantidad * precio_unitario
        precio_con_descuento = precio_sin_descuento * (1 - descuento / 100)
        return precio_con_descuento * (1 + impuesto / 100)

if __name__ == '__main__':
    calculadora = Calculadora()
    cantidad =2000
    precio_unitario=1.5
    descuento = 10
    impuesto =8

    print(f"Cantidad : {cantidad}")
    print(f"Precio unitario : {precio_unitario}")
    print(f"Descuento : {descuento}%")
    print(f"Impuesto : {impuesto}%")
    print(f"Precio Total: {calculadora.calcular_precio_total(cantidad, precio_unitario, descuento, impuesto)}")