import unittest

import sys
sys.path.append("src")

from model import hipoteca_inversa

class PruebasHipotecaInversa(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Hipoteca.
    """

    # Casos de prueba normales
    def test_hipoteca_normal_1(self):
        """
        Prueba el cálculo de la hipoteca inversa con valores normales.
        """
        edad = 70
        total_cuotas = 60
        precio_de_la_vivienda = 200_000_000
        porcentaje_precio_real = 30
        tasa_de_interes_mensual = 10

        resultado_ingreso_mensual_esperado = 1_000_000
        resultado_deuda_total_esperada = 3_338_298_035

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 1")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_hipoteca_normal_2(self):
        """
        Prueba el cálculo de la hipoteca inversa con valores normales.
        """
        edad = 75
        total_cuotas = 156
        precio_de_la_vivienda = 412_949_945
        porcentaje_precio_real = 50
        tasa_de_interes_mensual = 5.50

        resultado_ingreso_mensual_esperado = 1_323_558
        resultado_deuda_total_esperada = 107_625_171_318

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 2")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_hipoteca_normal_3(self):
        """
        Prueba el cálculo de la hipoteca inversa con valores normales.
        """
        edad = 85
        total_cuotas = 48
        precio_de_la_vivienda = 619_424_917
        porcentaje_precio_real = 40
        tasa_de_interes_mensual = 4.80

        resultado_ingreso_mensual_esperado = 5_161_874
        resultado_deuda_total_esperada = 957_016_422

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 3")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    # Casos de prueba extraordinarios
    def test_hipoteca_cuota_unica(self):
        """
        Prueba el cálculo de la hipoteca inversa con una sola cuota.
        """
        edad = 70
        total_cuotas = 1
        precio_de_la_vivienda = 908_489_879
        porcentaje_precio_real = 55
        tasa_de_interes_mensual = 1.20

        resultado_ingreso_mensual_esperado = 499_669_433
        resultado_deuda_total_esperada = 505_665_467

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 1")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_hipoteca_tasa_cero(self):
        """
        Prueba el cálculo de la hipoteca inversa con tasa de interés igual a 0.
        """
        edad = 78
        total_cuotas = 144
        precio_de_la_vivienda = 1_238_849_835
        porcentaje_precio_real = 50
        tasa_de_interes_mensual = 0

        resultado_ingreso_mensual_esperado = 4_301_562
        resultado_deuda_total_esperada = 619_424_918

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 2")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_hipoteca_porcentaje_100(self):
        """
        Prueba el cálculo de la hipoteca inversa con porcentaje del precio real igual a 100%.
        """
        edad = 76
        total_cuotas = 144
        precio_de_la_vivienda = 743_309_901
        porcentaje_precio_real = 100
        tasa_de_interes_mensual = 1.1

        resultado_ingreso_mensual_esperado = 5_161_874
        resultado_deuda_total_esperada = 1_818_198_009

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 3")
        print("Advertencia: La hipoteca cubre el 100% del precio de la vivienda.")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    # Casos de prueba con errores
    def test_error_porcentajes_negativos(self):
        """
        Prueba el error al usar porcentajes negativos.
        """
        edad = 74
        total_cuotas = 168
        precio_de_la_vivienda = 1_032_374_862
        porcentaje_precio_real = -5.0
        tasa_de_interes_mensual = -2.8

        with self.assertRaises(hipoteca_inversa.ErrorValoresIngresadosPorcentajes):
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

    def test_error_edad_invalida(self):
        """
        Prueba el error al usar una edad menor a 65.
        """
        edad = 50
        total_cuotas = 360
        precio_de_la_vivienda = 825_899_890
        porcentaje_precio_real = 45
        tasa_de_interes_mensual = 6

        with self.assertRaises(hipoteca_inversa.ErrorEdadIncorrecta):
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

    def test_error_cuotas_invalidas(self):
        """
        Prueba el error al usar un número de cuotas inválido.
        """
        edad = 80
        total_cuotas = 0
        precio_de_la_vivienda = 1_238_849_835
        porcentaje_precio_real = 50
        tasa_de_interes_mensual = 5

        with self.assertRaises(hipoteca_inversa.ErrorCuotas):
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

    def test_error_edad_negativa(self):
        """
        Prueba el error al usar una edad negativa.
        """
        edad = -65
        total_cuotas = 168
        precio_de_la_vivienda = 619_424_917
        porcentaje_precio_real = 40
        tasa_de_interes_mensual = 2.3

        with self.assertRaises(hipoteca_inversa.ErrorEdadnegativa):
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

if __name__ == '__main__':
    unittest.main()