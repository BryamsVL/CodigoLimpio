class Datos:
    def procesar_dato(self, dato):
        return dato * 2 if dato > 10 else dato * 3

    def procesar_datos(self, datos):
        return [self.procesar_dato(dato) for dato in datos]


if __name__ == '__main__':
    pass