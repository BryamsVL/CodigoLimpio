class Calculadora:
    def sumar_numeros(self, primer_numero, segundo_numero):
        return primer_numero + segundo_numero


if __name__ == '__main__':
    caculadora = Calculadora()
    sumando1=4
    sumando2=10
    print(f"{sumando1} + {sumando2} = {caculadora.sumar_numeros(sumando1,sumando2)}")