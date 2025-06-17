import unittest
from queue import Queue as Cola
from parcial import tuplas_positivas_y_negativas

class Ej3Test(unittest.TestCase):
    def setUp(self):
        self.method = tuplas_positivas_y_negativas

    def test_elimina_tuplas_nulas(self):
        entrada = construir_cola_con_elementos([(-1, -1), (0, 0), (1, 1), (0, 4), (-2, 1)])
        salida_esperada = construir_cola_con_elementos([(-1, -1), (1, 1), (-2, 1)])
        self.method(entrada)
        self.assertEqual(list(entrada.queue), list(salida_esperada.queue))

    def test_todas_positivas_queda_igual(self):
        entrada = construir_cola_con_elementos([(1, 1), (1, 2), (3, 4)])
        salida_esperada = construir_cola_con_elementos([(1, 1), (1, 2), (3, 4)])
        self.method(entrada)
        self.assertEqual(list(entrada.queue), list(salida_esperada.queue))

    def test_todas_negativas_queda_igual(self):
        entrada = construir_cola_con_elementos([(1, -1), (-1, 2), (-3, 4)])
        salida_esperada = construir_cola_con_elementos([(1, -1), (-1, 2), (-3, 4)])
        self.method(entrada)
        self.assertEqual(list(entrada.queue), list(salida_esperada.queue))

    def test_todas_nulas(self):
        entrada = construir_cola_con_elementos([(0, 0)])
        salida_esperada = Cola()
        self.method(entrada)
        self.assertEqual(list(entrada.queue), list(salida_esperada.queue))

    def test_tuplas_negativas_antes_que_positivas(self):
        entrada = construir_cola_con_elementos([(-1, 2), (-1, -1), (1, -2), (2, 2)])
        salida_esperada = construir_cola_con_elementos([(-1, -1), (2, 2), (-1, 2), (1, -2)])
        self.method(entrada)
        self.assertEqual(list(entrada.queue), list(salida_esperada.queue))

    def test_tuplas_negativas_antes_que_positivas_y_nulas(self):
        entrada = construir_cola_con_elementos([(-1, 2), (-1, -1), (1, -2), (0, 0), (2, 2)])
        salida_esperada = construir_cola_con_elementos([(-1, -1), (2, 2), (-1, 2), (1, -2)])
        self.method(entrada)
        self.assertEqual(list(entrada.queue), list(salida_esperada.queue))

    def test_tuplas_intercaladas(self):
        entrada = construir_cola_con_elementos([(1, 2), (1, -2), (-1, -2), (1, 0), (0, 2), (0, 0), (3, 2)])
        salida_esperada = construir_cola_con_elementos([(1, 2), (3, 2), (1, -2), (-1, -2)])
        self.method(entrada)
        self.assertEqual(list(entrada.queue), list(salida_esperada.queue))

    def test_vacio(self):
        entrada = Cola()
        salida_esperada = Cola()
        self.method(entrada)
        self.assertEqual(list(entrada.queue), list(salida_esperada.queue))

def construir_cola_con_elementos(elementos: list[tuple[int, int]]) -> Cola:
    res = Cola()
    for elem in elementos:
        res.put(elem)
    return res

if __name__ == '__main__':
    unittest.main(verbosity=2)
