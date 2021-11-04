import unittest
from generala import *
from jugador import Jugador


class TestTiro(unittest.TestCase):

    def test_tirar_dados(self):
        juego = Juego()
        dados = juego.tirarDados()
        self.assertEqual(len(dados), 5)

    def test_isGenerala(self):
        juego = Juego()
        dados = [1, 1, 1, 1, 1]
        self.assertTrue(juego.isGenerala(dados))

    def test_notGenerala(self):
        juego = Juego()
        dados = [1, 1, 2, 1, 1]
        self.assertFalse(juego.isGenerala(dados))

    def test_isPoker(self):
        juego = Juego()
        dados = [2, 2, 2, 2, 3]
        self.assertTrue(juego.isPoker(dados))

    def test_isPoker2(self):
        juego = Juego()
        dados = [2, 2, 2, 1, 2]
        self.assertTrue(juego.isPoker(dados))

    def test_notPoker(self):
        juego = Juego()
        dados = [1, 2, 1, 2, 2]
        self.assertFalse(juego.isPoker(dados))

    def test_notPoker2(self):
        juego = Juego()
        dados = [5, 1, 1, 6, 6]
        self.assertFalse(juego.isPoker(dados))

    def test_isFull1(self):
        juego = Juego()
        dados = [1, 1, 1, 2, 2]
        self.assertTrue(juego.isFull(dados))

    def test_isFull2(self):
        juego = Juego()
        dados = [1, 2, 1, 1, 2]
        self.assertTrue(juego.isFull(dados))

    def test_notFull(self):
        juego = Juego()
        dados = [1, 2, 1, 3, 2]
        self.assertFalse(juego.isFull(dados))

    def test_isEscaleraOrdenada(self):
        juego = Juego()
        dados = [1, 2, 3, 4, 5]
        self.assertTrue(juego.isEscalera(dados))

    def test_isEscaleraDesordenada(self):
        juego = Juego()
        dados = [1, 3, 4, 2, 6]
        self.assertTrue(juego.isEscalera(dados))

    def test_notEscalera(self):
        juego = Juego()
        dados = [1, 2, 3, 4, 4]
        self.assertFalse(juego.isEscalera(dados))


class TestGrilla(unittest.TestCase):

    def test_estado_grilla_OK(self):
        juego = Juego()
        j = Jugador()
        self.assertTrue(juego.estadoGrilla(j, 'generala'))
        self.assertTrue(juego.puedeJugar)

    def test_estado_grilla_jugada_anotada(self):
        juego = Juego()
        j = Jugador()
        juego.anotar(j, 'generala', [1, 1, 1, 1, 1])
        self.assertFalse(juego.puedeJugar)

    def test_estado_grilla_jugada_anotada_ERROR(self):
        juego = Juego()
        j = Jugador()
        j.miGrilla['generala'] = 50
        with self.assertRaises(TablaError):
            juego.estadoGrilla(j, 'generala')

    def test_estad_grilla_jugada_noexiste_ERROR(self):
        juego = Juego()
        j = Jugador()
        with self.assertRaises(InputError):
            juego.estadoGrilla(j, 'pancho')

    def test_anotar_uno_1(self):
        juego = Juego()
        j = Jugador()
        dados = [2, 5, 3, 4, 1]
        juego.anotar(j, '1', dados)
        self.assertEqual(j.miGrilla['1'], 1)

    def test_anotar_uno_3(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 5, 1, 4, 1]
        juego.anotar(j, '1', dados)
        self.assertEqual(j.miGrilla['1'], 3)

    def test_anotar_uno_5(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 1, 1, 1, 1]
        juego.anotar(j, '1', dados)
        self.assertEqual(j.miGrilla['1'], 5)

    ####################################################
    def test_anotar_dos_1(self):
        juego = Juego()
        j = Jugador()
        dados = [2, 5, 1, 4, 1]
        juego.anotar(j, '2', dados)
        self.assertEqual(j.miGrilla['2'], 2)

    def test_anotar_dos_3(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 5, 2, 2, 1]
        juego.anotar(j, '2', dados)
        self.assertEqual(j.miGrilla['2'], 4)

    def test_anotar_dos_5(self):
        juego = Juego()
        j = Jugador()
        dados = [2, 2, 2, 2, 2]
        juego.anotar(j, '2', dados)
        self.assertEqual(j.miGrilla['2'], 10)

    ####################################################
    def test_anotar_tres_1(self):
        juego = Juego()
        j = Jugador()
        dados = [3, 5, 1, 4, 1]
        juego.anotar(j, '3', dados)
        self.assertEqual(j.miGrilla['3'], 3)

    def test_anotar_tres_3(self):
        juego = Juego()
        j = Jugador()
        dados = [3, 5, 3, 4, 3]
        juego.anotar(j, '3', dados)
        self.assertEqual(j.miGrilla['3'], 9)

    def test_anotar_tres_5(self):
        juego = Juego()
        j = Jugador()
        dados = [3, 3, 3, 3, 3]
        juego.anotar(j, '3', dados)
        self.assertEqual(j.miGrilla['3'], 15)

    ####################################################
    def test_anotar_cuatro_1(self):
        juego = Juego()
        j = Jugador()
        dados = [6, 5, 1, 4, 1]
        juego.num_lanzamiento = 2
        juego.anotar(j, '4', dados)
        self.assertEqual(j.miGrilla['4'], 4)

    def test_anotar_cuatro_3(self):
        juego = Juego()
        j = Jugador()
        dados = [4, 4, 3, 4, 3]
        juego.anotar(j, '4', dados)
        self.assertEqual(j.miGrilla['4'], 12)

    def test_anotar_cuatro_5(self):
        juego = Juego()
        j = Jugador()
        dados = [4, 4, 4, 4, 4]
        juego.anotar(j, '4', dados)
        self.assertEqual(j.miGrilla['4'], 20)

    ####################################################
    def test_anotar_cinco_1(self):
        juego = Juego()
        j = Jugador()
        dados = [6, 5, 1, 4, 1]
        juego.anotar(j, '5', dados)
        self.assertEqual(j.miGrilla['5'], 5)

    def test_anotar_cinco_3(self):
        juego = Juego()
        j = Jugador()
        dados = [5, 5, 3, 5, 3]
        juego.anotar(j, '5', dados)
        self.assertEqual(j.miGrilla['5'], 15)

    def test_anotar_cinco_5(self):
        juego = Juego()
        j = Jugador()
        dados = [5, 5, 5, 5, 5]
        juego.anotar(j, '5', dados)
        self.assertEqual(j.miGrilla['5'], 25)

    ####################################################
    def test_anotar_seis_1(self):
        juego = Juego()
        j = Jugador()
        dados = [6, 5, 1, 4, 1]
        juego.anotar(j, '6', dados)
        self.assertEqual(j.miGrilla['6'], 6)

    def test_anotar_seis_3(self):
        juego = Juego()
        j = Jugador()
        dados = [6, 5, 6, 4, 6]
        juego.anotar(j, '6', dados)
        self.assertEqual(j.miGrilla['6'], 18)

    def test_anotar_seis_5(self):
        juego = Juego()
        j = Jugador()
        dados = [6, 6, 6, 6, 6]
        juego.anotar(j, '6', dados)
        self.assertEqual(j.miGrilla['6'], 30)

    ####################################################

    def test_anotar_escalera_servida(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 2, 3, 4, 5]
        juego.num_lanzamiento = 1
        juego.anotar(j, 'escalera', dados)
        self.assertEqual(j.miGrilla['escalera'], 25)

    def test_anotar_escalera(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 2, 3, 4, 5]
        juego.num_lanzamiento = 2
        juego.anotar(j, 'escalera', dados)
        self.assertEqual(j.miGrilla['escalera'], 20)

    ####################################################
    def test_anotar_full_servido(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 1, 3, 3, 3]
        juego.num_lanzamiento = 1
        juego.anotar(j, 'full', dados)
        self.assertEqual(j.miGrilla['full'], 35)

    def test_anotar_full(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 1, 3, 3, 3]
        juego.num_lanzamiento = 2
        juego.anotar(j, 'full', dados)
        self.assertEqual(j.miGrilla['full'], 30)

    ####################################################
    def test_anotar_poker_servido(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 3, 3, 3, 3]
        juego.num_lanzamiento = 1
        juego.anotar(j, 'poker', dados)
        self.assertEqual(j.miGrilla['poker'], 45)

    def test_anotar_poker(self):
        juego = Juego()
        j = Jugador()
        dados = [1, 3, 3, 3, 3]
        juego.num_lanzamiento = 2
        juego.anotar(j, 'poker', dados)
        self.assertEqual(j.miGrilla['poker'], 40)

    ####################################################
    def test_anotar_generala_servida(self):
        juego = Juego()
        j = Jugador()
        dados = [3, 3, 3, 3, 3]
        juego.num_lanzamiento = 1
        juego.anotar(j, 'generala', dados)
        self.assertEqual(j.miGrilla['generala'], 55)

    def test_anotar_generala(self):
        juego = Juego()
        j = Jugador()
        dados = [3, 3, 3, 3, 3]
        juego.num_lanzamiento = 2
        juego.anotar(j, 'generala', dados)
        self.assertEqual(j.miGrilla['generala'], 50)

    ####################################################
    def test_anotar_doble_generala(self):
        juego = Juego()
        j = Jugador()
        dados = [3, 3, 3, 3, 3]
        j.miGrilla['generala'] = 50
        juego.anotar(j, 'doble generala', dados)
        self.assertEqual(j.miGrilla['doble generala'], 100)


class TurnoTest(unittest.TestCase):

    def test_tirada_1(self):
        juego = Juego()
        juego.tirarDados()
        self.assertEqual(juego.num_lanzamiento, 1)

    def test_tirada_2(self):
        juego = Juego()
        juego.tirarDados()
        juego.tirarDados()
        self.assertEqual(juego.num_lanzamiento, 2)

    def test_tirada_3(self):
        juego = Juego()
        juego.tirarDados()
        juego.tirarDados()
        juego.tirarDados()
        self.assertEqual(juego.num_lanzamiento, 3)

    # El contador debe quedar en 3 ya que no avanza al turno numero 4
    def test_tirada_4_Error(self):
        juego = Juego()
        juego.tirarDados()
        juego.tirarDados()
        juego.tirarDados()
        juego.tirarDados()
        self.assertEqual(juego.num_lanzamiento, 3)
        with self.assertRaises(TurnoError):
            juego.siguiente_lanzamiento()

    def test_turnos_alcanzados(self):
        juego = Juego()
        juego.turnos = 0
        with self.assertRaises(TurnoError):
            juego.siguiente_turno()

    def test_siguiente_turno(self):
        juego = Juego()
        juego.turnos = 11
        juego.siguiente_turno()
        self.assertEqual(juego.turnos, 10)


class TestMostrar(unittest.TestCase):

    def test_mostrar_jugada_gs(self):
        juego = Juego()
        dados = [1, 1, 1, 1, 1]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.mostrarTirada(dados), 'gs')

    def test_mostrar_jugada_g(self):
        juego = Juego()
        dados = [1, 1, 1, 1, 1]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.mostrarTirada(dados), 'g')

    def test_mostrar_jugada_fs(self):
        juego = Juego()
        dados = [2, 2, 1, 1, 1]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.mostrarTirada(dados), 'fs')

    def test_mostrar_jugada_f(self):
        juego = Juego()
        dados = [2, 2, 1, 1, 1]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.mostrarTirada(dados), 'f')

    def test_mostrar_jugada_ps(self):
        juego = Juego()
        dados = [2, 1, 1, 1, 1]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.mostrarTirada(dados), 'ps')

    def test_mostrar_jugada_p(self):
        juego = Juego()
        dados = [2, 1, 1, 1, 1]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.mostrarTirada(dados), 'p')

    def test_mostrar_jugada_es(self):
        juego = Juego()
        dados = [1, 2, 3, 4, 5]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.mostrarTirada(dados), 'es')

    def test_mostrar_jugada_e(self):
        juego = Juego()
        dados = [1, 2, 3, 4, 5]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.mostrarTirada(dados), 'e')

    def test_mostrar_jugada_n(self):
        juego = Juego()
        dados = [1, 3, 3, 4, 5]
        self.assertEqual(juego.mostrarTirada(dados), 'n')


class TestVerificarJugada(unittest.TestCase):

    def test_verificar_doble_generala(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,1,1,1,1]
        jugador.miGrilla['generala'] = 50
        self.assertEqual(juego.verificarTirada(jugador,'doble generala',dados), 100)

    def test_verificar_doble_generala_ERROR(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1, 1, 1, 1, 1]
        with self.assertRaises(TablaError):
            juego.verificarTirada(jugador,'doble generala',dados)

    def test_verificar_generala_servida(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,1,1,1,1]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.verificarTirada(jugador,'generala',dados), 55)

    def test_verificar_generala(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,1,1,1,1]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.verificarTirada(jugador,'generala',dados), 50)

    def test_verificar_NOgenerala(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,1,1,2,2]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.verificarTirada(jugador,'generala',dados), 0)

    def test_verificar_poker_servido(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,1,1,1,1]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.verificarTirada(jugador,'poker',dados), 45)

    def test_verificar_poker(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,1,1,1,1]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.verificarTirada(jugador,'poker',dados), 40)

    def test_verificar_NOpoker(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,1,1,3,1]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.verificarTirada(jugador,'poker',dados), 0)

    def test_verificar_full_servido(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,2,1,1,1]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.verificarTirada(jugador,'full',dados), 35)

    def test_verificar_full(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,2,1,1,1]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.verificarTirada(jugador,'full',dados), 30)

    def test_verificar_NOfull(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,2,1,1,4]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.verificarTirada(jugador,'full',dados), 0)

    def test_verificar_escalera_servida(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,3,4,5,6]
        juego.num_lanzamiento = 1
        self.assertEqual(juego.verificarTirada(jugador,'escalera',dados), 25)

    def test_verificar_escalera(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,3,4,5,6]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.verificarTirada(jugador,'escalera',dados), 20)

    def test_verificar_NOescalera(self):
        juego = Juego()
        jugador = Jugador()
        dados = [2,3,2,5,6]
        juego.num_lanzamiento = 2
        self.assertEqual(juego.verificarTirada(jugador,'escalera',dados), 0)

    def test_verificar_uno(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,1,1,2,3]
        self.assertEqual(juego.verificarTirada(jugador,'1',dados), 3)

    def test_verificar_NOuno(self):
        juego = Juego()
        jugador = Jugador()
        dados = [6,3,3,2,3]
        self.assertEqual(juego.verificarTirada(jugador,'1',dados), 0)

    def test_verificar_dos(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,2,1,2,3]
        self.assertEqual(juego.verificarTirada(jugador,'2',dados), 4)

    def test_verificar_NOdos(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,4,1,5,3]
        self.assertEqual(juego.verificarTirada(jugador,'2',dados), 0)

    def test_verificar_tres(self):
        juego = Juego()
        jugador = Jugador()
        dados = [3,3,3,2,3]
        self.assertEqual(juego.verificarTirada(jugador,'3',dados), 12)

    def test_verificar_cuatro(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,4,4,2,3]
        self.assertEqual(juego.verificarTirada(jugador,'4',dados), 8)

    def test_verificar_cinco(self):
        juego = Juego()
        jugador = Jugador()
        dados = [1,1,5,5,3]
        self.assertEqual(juego.verificarTirada(jugador,'5',dados), 10)

    def test_verificar_seis(self):
        juego = Juego()
        jugador = Jugador()
        dados = [6,6,1,6,3]
        self.assertEqual(juego.verificarTirada(jugador,'6',dados), 18)


class TestFinal(unittest.TestCase):

    def test_fin_juego(self):
        juego = Juego()
        j1 = Jugador("pepe")
        j2 = Jugador("juanito")
        juego.lista_jugadores = [j1, j2]

        j1.miGrilla['1'] = 1
        j1.miGrilla['2'] = 1
        j1.miGrilla['3'] = 1
        j1.miGrilla['4'] = 1
        j1.miGrilla['5'] = 1
        j1.miGrilla['6'] = 1
        j1.miGrilla['escalera'] = 1
        j1.miGrilla['full'] = 1
        j1.miGrilla['poker'] = 1
        j1.miGrilla['generala'] = 1
        j1.miGrilla['doble generala'] = 1

        j2.miGrilla['1'] = 0
        j2.miGrilla['2'] = 0
        j2.miGrilla['3'] = 0
        j2.miGrilla['4'] = 0
        j2.miGrilla['5'] = 0
        j2.miGrilla['6'] = 0
        j2.miGrilla['escalera'] = 0
        j2.miGrilla['full'] = 0
        j2.miGrilla['poker'] = 0
        j2.miGrilla['generala'] = 0
        j2.miGrilla['doble generala'] = 100

        self.assertEqual(juego.fin_juego(), 'JUANITO')


if __name__ == '__main__':
    unittest.main()
