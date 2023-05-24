from unittest import TestCase
from crud.CrudCliente import CrudCliente
from crud.CrudControlFertilizantes import CrudControlFertilizantes
from crud.CrudControlPlagas import CrudControlPlagas
from crud.CrudAntibiotico import CrudAntibiotico
from crud.CrudFacturas import CrudFacturas
from model.ProductoControl import ProductoControl
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.producto1 = CrudControlFertilizantes.crear_fertilizante("110001098", "Asocrece", "cada 45 días", 850000, "09/02/2023")
        self.producto2 = CrudControlPlagas.crear_plaga("250048172", "Quimicalplags", "cada 15 días", 700000, "20 días")
        self.producto3 = CrudAntibiotico.crear_antibiotico("Curazoo", "500kg", "Bovinos", 500000)

        self.cliente1 = CrudCliente.crear_cliente("Luis Sebastian Conde Toro", "1004756531")

        self.factura1 = CrudFacturas.crear_Factura()
        self.factura2 = CrudFacturas.crear_Factura()

    def test_factura_asociadas_cliente(self):
        self.cliente1.agregar_factura(self.factura1)
        self.cliente1.agregar_factura(self.factura2)
        self.assertEqual(2, self.cliente1.facturas_asociadas())

    def test_agregar_producto_a_factura(self):
        CrudFacturas.actualizar_factura(self.factura1, self.producto1, 2)
        CrudFacturas.actualizar_factura(self.factura1, self.producto2, 1)
        CrudFacturas.actualizar_factura(self.factura1, self.producto3, 3)
        self.assertEqual(6, self.factura1.numero_productos_comprados())

    def test_herencia_producto_control(self):
        #ADVERTENCIA: ¡Para que la prueba sea correcta solo se debe poner 0 en el valor del producto!
        producto_control = ProductoControl("250048172", "Quimicalplags", "cada 15 días", 0)
        self.assertEqual(float(producto_control.obtener_valor()), 0)

        control_plagas = CrudControlPlagas.crear_plaga("250048172", "Quimicalplags", "cada 15 días", 0, "20 días")
        self.assertIsInstance(control_plagas, ProductoControl)
        self.assertEqual(float(control_plagas.obtener_valor()), 0)

        control_fertilizantes = CrudControlFertilizantes.crear_fertilizante("110001098", "Asocrece", "cada 45 días", 0, "09/02/2023")
        self.assertIsInstance(control_fertilizantes, ProductoControl)
        self.assertEqual(float(control_fertilizantes.obtener_valor()), 0)

    def test_crear_cliente(self):
        cliente = CrudCliente.crear_cliente("John Doe", "1234567890")

        # Verificar que el cliente se ha creado correctamente
        self.assertEqual(cliente.obtener_cedula(), "1234567890")


    def test_crear_cliente(self):
        cliente = CrudCliente.crear_cliente("Luis Conde", "1234567890")
        clientes_registrados = CrudCliente.obtener_clientes_registrados()
        self.assertIn(cliente, clientes_registrados)


    def test_buscar_por_cedula(self):
        cliente = CrudCliente.crear_cliente("Carlos Toro", "1234567890")
        cliente_encontrado = CrudCliente.buscar_por_cedula("1234567890")
        self.assertEqual(cliente, cliente_encontrado)


    def test_actualizar_nombre_cliente(self):
        cliente = CrudCliente.crear_cliente("Marta Jimenez", "012345896")
        CrudCliente.actualizar_nombre_cliente("012345896", "Jane Smith")
        cliente_actualizado = CrudCliente.buscar_por_cedula("012345896")
        self.assertEqual(cliente_actualizado.obtener_nombre(), "Jane Smith")


    def test_eliminar_cliente(self):
        cliente = CrudCliente.crear_cliente("Daniel Alvarez", "357901234")
        CrudCliente.eliminar_cliente("357901234")
        clientes_registrados = CrudCliente.obtener_clientes_registrados()
        self.assertNotIn(cliente, clientes_registrados)


    def test_numero_clientes_registrados(self):
        CrudCliente.eliminar_todos_los_clientes()
        self.assertEqual(CrudCliente.numero_clientes_registrados(), 0)

        CrudCliente.crear_cliente("Ana Mendez", "1234567890")
        CrudCliente.crear_cliente("Jane Smith", "0987654321")

        self.assertEqual(CrudCliente.numero_clientes_registrados(), 2)


if __name__ == '__main__':
    unittest.main()
