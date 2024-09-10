class Datos:
    def procesar_datos(self, datos):
        resultado = []
        for dato in datos:
            if dato > 10:
                resultado.append(dato * 2)
            else:
                resultado.append(dato * 3)
        return resultado

if __name__ == '__main__':
    pass