class Jugador:
    def __init__(self, nombre=''):
        self.nombre = nombre.upper()
        self.miGrilla = {
            '1': None,
            '2': None,
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            'escalera': None,
            'full': None,
            'poker': None,
            'generala': None,
            'doble generala': None
        }

    def __str__(self):
        return "Nombre: {}".format(self.nombre)

    def miGrilla_str(self):
        return "|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|uno:{}           \n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|dos:{}           " \
               "\n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|tres:{}          \n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|cuatro:{}        " \
               "\n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|cinco:{}         \n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|seis:{}          " \
               "\n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|escalera:{}      \n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|full:{}          " \
               "\n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|poker:{}         \n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|generala:{}      " \
               "\n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n|doble generala:{}\n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯".format(self.miGrilla['1'],
                                                                                         self.miGrilla['2'],
                                                                                         self.miGrilla['3'],
                                                                                         self.miGrilla['4'],
                                                                                         self.miGrilla['5'],
                                                                                         self.miGrilla['6'],
                                                                                         self.miGrilla['escalera'],
                                                                                         self.miGrilla['full'],
                                                                                         self.miGrilla['poker'],
                                                                                         self.miGrilla['generala'],
                                                                                         self.miGrilla['doble generala']
                                                                                         )

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def miGrilla(self):
        return self.__miGrilla

    @miGrilla.setter
    def miGrilla(self, value):
        self.__miGrilla = value


if __name__ == '__main__':
    j = Jugador("pepe")
    print(j)
