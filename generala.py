from functools import reduce
from random import randint
from jugador import Jugador


class TablaError(Exception):
    pass


class TurnoError(Exception):
    pass


class InputError(Exception):
    pass


class Juego:
    def __init__(self):
        self.MENU = "Qué desea hacer? \n1.Volver a tirar\n2.Marcar casilla\n>>"
        self.MENU2 = "VOLVER A TIRAR\n1.Volver a tirar todo\n2.Elegir dados para tirar\n3.Atrás\n>>"
        self.lista_jugadores = []
        self.num_lanzamiento = 0
        self.turnos = 0
        self.rondas = 11  # El juego consta de 11 rondas (11 casillas a que deben ser marcadas en un turno si o si)
        self.puedeJugar = True

    def crearJugadores(self):
        while True:
            try:
                cant = int(input("Cantidad de jugadores >> "))
                for i in range(cant):
                    nuevo_jugador = Jugador()
                    nuevo_jugador.nombre = input("Nombre del jugador {} >>".format(i + 1).upper())
                    self.lista_jugadores.append(nuevo_jugador)
                break
            except Exception as e:
                print("ERROR-----Ingresa un numero entero")

    def tirarDados(self):
        try:
            self.siguiente_lanzamiento()
            dados = []
            for d in range(5):
                dados.append(randint(1, 6))
            return dados
        except TurnoError as e:
            print(e)

    def tirarSeleccionados(self, dados):
        try:
            self.siguiente_lanzamiento()
            repe = []  # repe sirve para guardar los dados que ya se seleccionaron para volver a tirar
            select = 1
            while select != 0:
                print("¿Qué dado desea volver a tirar? Ingrese 0 para terminar\n>>")
                print(dados)
                self.mostrarTirada(dados)
                select = int(input())
                if 0 <= select <= 5:
                    if select not in repe:
                        if select == 1:
                            dados[0] = randint(1, 6)
                            repe.append(1)
                        if select == 2:
                            dados[1] = randint(1, 6)
                            repe.append(2)
                        if select == 3:
                            dados[2] = randint(1, 6)
                            repe.append(3)
                        if select == 4:
                            dados[3] = randint(1, 6)
                            repe.append(4)
                        if select == 5:
                            dados[4] = randint(1, 6)
                            repe.append(5)
                    else:
                        raise TurnoError("ERROR-------En un turno no se puede tirar el mismo dado")
                    if len(repe) == 5:
                        print("ERROR-------Ya tiraste todos los dados de nuevo de este turno")
                else:
                    raise InputError("ERROR--------INGRESE UN NUMERO DEL 1 AL 5")
            return dados
        except TurnoError as e:
            print(e)

    # isGenerala verifica que todos los dados sean iguales
    @staticmethod
    def isGenerala(dados):
        if len(set(dados)) == 1:
            return True
        else:
            return False

    # isPoker verifica que 4 dados sean iguales
    @staticmethod
    def isPoker(dados):
        repetidos = [0] * 6
        for dado in dados:
            index = dado - 1
            repetidos[index] += 1
        if 4 in repetidos:
            return True
        else:
            return False

    # isFull verifica que 2 dados sean iguales y que 3 dados sean iguales
    @staticmethod
    def isFull(dados):
        hay_tres = False
        hay_dos = False
        for i in range(0, len(dados)):
            if dados.count(dados[i]) == 3:
                hay_tres = True
            if dados.count(dados[i]) == 2:
                hay_dos = True
        if hay_dos and hay_tres:
            return True
        else:
            return False

    # isEscalera verifica que no se repita ningun dado
    @staticmethod
    def isEscalera(dados):
        if len(set(dados)) == 5:
            return True
        else:
            return False

    # funcion con fines graficos
    def mostrarTirada(self, dados):
        if self.isGenerala(dados):
            if self.num_lanzamiento == 1:
                print("Generala Servida!")
                return 'gs'
            else:
                print("Generala!")
                return 'g'
        elif self.isPoker(dados):
            if self.num_lanzamiento == 1:
                print("Poker Servido!")
                return 'ps'
            else:
                print("Poker!")
                return 'p'
        elif self.isFull(dados):
            if self.num_lanzamiento == 1:
                print("Full Servido!")
                return 'fs'
            else:
                print("Full!")
                return 'f'
        elif self.isEscalera(dados):
            if self.num_lanzamiento == 1:
                print("Escalera Servida!")
                return 'es'
            else:
                print("Escalera!")
                return 'e'
        else:
            print("Nada")
            return 'n'

    # funcion que verifica y devuelve los puntos correspondientes al input del usuario
    def verificarTirada(self, jugador, jugada, dados):
        puntos = 0
        if jugada == "escalera":
            if self.isEscalera(dados):
                if self.num_lanzamiento == 1:
                    puntos = 25
                else:
                    puntos = 20
        elif jugada == "full":
            if self.isFull(dados):
                if self.num_lanzamiento == 1:
                    puntos = 35
                else:
                    puntos = 30
        elif jugada == "poker":
            if self.isPoker(dados):
                if self.num_lanzamiento == 1:
                    puntos = 45
                else:
                    puntos = 40
        elif jugada == "generala":
            if self.isGenerala(dados):
                if self.num_lanzamiento == 1:
                    puntos = 55
                else:
                    puntos = 50
        elif jugada == "doble generala":
            if self.isGenerala(dados):
                if jugador.miGrilla['generala'] is not None:
                    puntos = 100
                else:
                    raise TablaError("Para marcar 'doble generala' primero debe tener 'generala'")
        else:
            for dado in dados:
                if jugada == str(dado):
                    puntos += dado

        return puntos

    def estadoGrilla(self, jugador, casilla):
        if casilla not in jugador.miGrilla.keys():
            raise InputError("ERROR-----Su ingreso no corresponde a ninguna jugada")
        if jugador.miGrilla[casilla] is None:
            self.puedeJugar = True
            return True
        else:
            raise TablaError("Esa casilla ya esta marcada, elija otra")

    def anotar(self, jugador, inputJugada, dados):
        try:
            grilla = jugador.miGrilla
            if self.estadoGrilla(jugador, inputJugada):
                puntos = self.verificarTirada(jugador, inputJugada, dados)
                grilla[inputJugada] = puntos
                self.puedeJugar = False
        except TablaError as e:
            print(e)
        except InputError as e:
            print(e)

    # funcion principal que funciona como menu
    def juega(self, jugador):
        try:
            self.puedeJugar = True
            self.num_lanzamiento = 0
            misDados = self.tirarDados()
            print("JUEGA: ", jugador.nombre.upper())

            while self.num_lanzamiento < 3:
                print(misDados)
                self.mostrarTirada(misDados)
                input1 = int(input(self.MENU))
                if input1 == 1:
                    self.menu2(misDados)
                elif input1 == 2:
                    break
                else:
                    raise InputError("Elija la opcion 1 o la opcion 2")

            while self.puedeJugar:
                print(jugador.miGrilla_str())
                marcar = input("Que casilla quiere marcar?\n >>")
                self.anotar(jugador, marcar, misDados)
        except TurnoError as e:
            print(e)

    def menu2(self, dados):
        try:

            input2 = int(input(self.MENU2))
            if input2 == 1:
                dados = self.tirarDados()
            if input2 == 2:
                dados = self.tirarSeleccionados(dados)
            if input2 == 3:
                pass
            return dados
        except InputError as e:
            print(e)
        except TurnoError as e:
            print(e)

    def siguiente_lanzamiento(self):
        if self.num_lanzamiento >= 3:
            raise TurnoError("Limite de lanzamientos alcanzado")
        self.num_lanzamiento += 1

    def siguiente_turno(self):
        if self.turnos == 0:
            raise TurnoError("FIN DEL JUEGO")
        self.turnos -= 1

    def fin_juego(self):
        fin_juego = {}
        print("PUNTAJES:\n")
        for jugador in self.lista_jugadores:
            grilla = jugador.miGrilla
            fin_juego[jugador.nombre] = reduce(lambda x, y: x + y[1], grilla.items(), 0)
            print("{} : {} PUNTOS".format(jugador.nombre, fin_juego[jugador.nombre]))

        ganador = max(fin_juego, key=fin_juego.get)
        print("----------------------------\n" \
              "     GANADOR ---->  " \
              + ganador + \
              "\n----------------------------")
        return ganador

    def main(self):
        try:

            self.crearJugadores()
            self.turnos = len(self.lista_jugadores) * self.rondas
            while self.turnos > 0:
                for jugador in self.lista_jugadores:
                    self.juega(jugador)
                    self.siguiente_turno()
            self.fin_juego()
        except InputError as e:
            print(e)
        except TablaError as e:
            print(e)
        except TurnoError as e:
            print(e)


if __name__ == '__main__':
    j = Juego()
    j.main()
