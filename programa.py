from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def main():
    """
    Función principal que maneja la interacción del usuario.

    Permite crear una tienda, ingresar productos, listar productos, realizar ventas y salir del programa.
    """

    print("Creación de una tienda")
    tipo_tienda = input("Ingrese el tipo de tienda (restaurante, supermercado, farmacia): ").strip().lower()
    nombre = input("Ingrese el nombre de la tienda: ").strip()
    costo_delivery = float(input("Ingrese el costo de delivery: ").strip())

    if tipo_tienda == "restaurante":
        tienda = Restaurante(nombre, costo_delivery)
    elif tipo_tienda == "supermercado":
        tienda = Supermercado(nombre, costo_delivery)
    elif tipo_tienda == "farmacia":
        tienda = Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    while True:
        print(
            "\nOpciones: 1) Ingresar producto 2) Listar productos 3) Realizar venta 4) Salir"
        )
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ").strip()
            precio_producto = float(input("Ingrese el precio del producto: ").strip())
            stock_producto = int(input("Ingrese el stock del producto: ").strip())
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
            print(f"Producto {nombre_producto} ingresado.")

        elif opcion == "2":
            print("Lista de productos:")
            print(tienda.listar_productos())

        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ").strip()
            cantidad = int(input("Ingrese la cantidad a vender: ").strip())
            tienda.realizar_venta(nombre_producto, cantidad)

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
