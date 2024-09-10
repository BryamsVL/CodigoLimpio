class Orden:
    def procesar_orden(self, orden):
        self.validar_orden(orden)
        self.guardar_orden_en_db(orden)
        self.enviar_confirmacion(orden)

if __name__ == '__main__':
    pass