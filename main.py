from crud.CrudCliente import CrudCliente
from crud.CrudControlFertilizantes import CrudControlFertilizantes
from crud.CrudControlPlagas import CrudControlPlagas
from crud.CrudAntibiotico import CrudAntibiotico
from crud.CrudFacturas import CrudFacturas

producto1 = CrudControlFertilizantes.crear_fertilizante("110001098", "Asocrece", "cada 45 días", 850000, "09/02/2023")
producto2 = CrudControlPlagas.crear_plaga("250048172", "Quimicalplags", "cada 15 días", 700000, "20 días")
producto3 = CrudAntibiotico.crear_antibiotico("Curazoo", "500kg", "Bovinos", 500000)

#--------------------------------------------------------------------------------------------------

cliente1 = CrudCliente.crear_cliente("Luis Sebastian Conde Toro", "1004756531")
cliente2 = CrudCliente.crear_cliente("Liliana Toro Gallego", "24173849")

factura1 = CrudFacturas.crear_Factura()
CrudFacturas.actualizar_factura(factura1, producto1, 2)
CrudFacturas.actualizar_factura(factura1, producto2, 1)

cliente1.agregar_factura(factura1)

cliente1.mostrar_cliente()

fecha = factura1.obtener_fecha


print(fecha)
print(type(factura1))
