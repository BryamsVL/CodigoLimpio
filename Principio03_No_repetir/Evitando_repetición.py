class Geometria:
    def area_rectangulo(self, ancho, alto=None):
        if alto is None:
            alto = ancho
        return ancho * alto

if __name__ == '__main__':
    pass