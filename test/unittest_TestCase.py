from unittest import TestCase
from crud.CrudCliente import CrudCliente
from crud.CrudControlFertilizantes import CrudControlFertilizantes
from crud.CrudControlPlagas import CrudControlPlagas
from crud.CrudAntibiotico import CrudAntibiotico
from crud.CrudFacturas import CrudFacturas
from model.ProductoControl import ProductoControl
from crud.ICrud import ICrud
import unittest

class MyTestCase(unittest.TestCase, ICrud):
    def setUp(self):
        crud_fertilizantes = CrudControlFertilizantes()
        crud_plagas = CrudControlPlagas()
        crud_antibioticos = CrudAntibiotico()
        self.producto1 = crud_fertilizantes.crear(registro_ICA="110001098", nombre_producto="Asocrece", frecuencia_aplicacion="cada 45 días", valor_producto=850000, ultima_aplicacion="09/02/2023")
        self.producto2 = crud_plagas.crear(registro_ICA="250048172", nombre_producto="Quimicalplags", frecuencia_aplicacion="cada 15 días", valor_producto=700000, periodo_carencia="20 días")
        self.producto3 = crud_antibioticos.crear(nombre_producto="Curazoo", dosis="500kg", tipo_animal="Bovinos", valor_producto=500000)
        crud_cliente = CrudCliente()
        self.cliente1 = crud_cliente.crear(nombre="Luis Sebastian Conde Toro", numero_cedula="1004756531")

        crud_factura1 = CrudFacturas()
        crud_factura2 = CrudFacturas()
        self.factura1 = crud_factura1.crear()
        self.factura2 = crud_factura2.crear()

    def test_factura_asociadas_cliente(self, **kwargs):
        self.cliente1.agregar_factura(self.factura1)
        self.cliente1.agregar_factura(self.factura2)
        self.assertEqual(2, self.cliente1.facturas_asociadas())

    def test_agregar_producto_a_factura(self, **kwargs):
        CrudFacturas.actualizar(factura=self.factura1, producto=self.producto1, cantidad=2)
        CrudFacturas.actualizar(factura=self.factura1, producto=self.producto2, cantidad=1)
        CrudFacturas.actualizar(factura=self.factura1, producto=self.producto3, cantidad=3)
        self.assertEqual(6, self.factura1.numero_productos_comprados())

    def test_herencia_producto_control(self, **kwargs):
        #ADVERTENCIA: ¡Para que la prueba sea correcta solo se debe poner 0 en el valor del producto!
        producto_control = ProductoControl("250048172", "Quimicalplags", "cada 15 días", 0)
        self.assertEqual(float(producto_control.obtener_valor), 0)
        crud_plagas = CrudControlPlagas()
        control_plagas = crud_plagas.crear(registro_ICA="250048172", nombre_producto="Quimicalplags", frecuencia_aplicacion="cada 15 días", valor_producto=0, periodo_carencia="20 días")
        self.assertIsInstance(control_plagas, ProductoControl)
        self.assertEqual(float(control_plagas.obtener_valor), 0)
        crud_fertilizantes = CrudControlFertilizantes()
        control_fertilizantes = crud_fertilizantes.crear(registro_ICA="110001098", nombre_producto="Asocrece", frecuencia_aplicacion="cada 45 días", valor_producto=0, ultima_aplicacion="09/02/2023")
        self.assertIsInstance(control_fertilizantes, ProductoControl)
        self.assertEqual(float(control_fertilizantes.obtener_valor), 0)

    def test_crear_cliente(self, **kwargs):
        crud_cliente = CrudCliente()
        cliente = crud_cliente.crear(nombre="John Doe", numero_cedula="1234567890")

        # Verificar que el cliente se ha creado correctamente
        self.assertEqual(cliente.obtener_cedula(), "1234567890")


    def test_crear_cliente(self, **kwargs):
        crud_cliente = CrudCliente()
        cliente = crud_cliente.crear(nombre="Luis Conde", numero_cedula="1234567890")
        clientes_registrados = CrudCliente.obtener_clientes_registrados()
        self.assertIn(cliente, clientes_registrados)


    def test_buscar_por_cedula(self, **kwargs):
        crud_cliente = CrudCliente()
        cliente = crud_cliente.crear(nombre="Carlos Toro", numero_cedula="1234567890")
        cliente_encontrado = CrudCliente.buscar(numero_cedula="1234567890")
        self.assertEqual(cliente, cliente_encontrado)


    def test_actualizar_nombre_cliente(self, **kwargs):
        crud_cliente = CrudCliente()
        cliente = crud_cliente.crear(nombre="Marta Jimenez", numero_cedula="012345896")
        crud_cliente.actualizar(numero_cedula="012345896", nombre_nuevo="Jane Smith")
        cliente_actualizado = CrudCliente.buscar(numero_cedula="012345896")
        self.assertEqual(cliente_actualizado.nombre_cliente, "Jane Smith")


    def test_eliminar_cliente(self):
        crud_cliente = CrudCliente()
        cliente = crud_cliente.crear(nombre="Daniel Alvarez", numero_cedula="357901234")
        CrudCliente.eliminar(numero_cedula="357901234")
        clientes_registrados = crud_cliente.obtener_clientes_registrados()
        self.assertNotIn(cliente, clientes_registrados)


    def test_numero_clientes_registrados(self):
        crud_cliente = CrudCliente()
        crud_cliente.eliminar_todos_los_clientes()
        self.assertEqual(CrudCliente.numero_clientes_registrados(), 0)

        crud_cliente.crear(nombre="Ana Mendez", numero_cedula="1234567890")
        crud_cliente.crear(nombre="Jane Smith", numero_cedula="0987654321")

        self.assertEqual(CrudCliente.numero_clientes_registrados(), 2)


if __name__ == '__main__':
    unittest.main()
