# Proyecto de Gestión de Tiendas

Este proyecto es una aplicación de consola que permite gestionar diferentes tipos de tiendas (restaurante, supermercado, farmacia). Los usuarios pueden crear una tienda, ingresar productos, listar productos y realizar ventas.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

- **`tienda.py`**: Define la clase base `Tienda` y sus métodos.
- **`producto.py`**: Define la clase `Producto` y sus métodos.
- **`programa.py`**: Contiene la función principal que maneja la interacción del usuario.
- **`restaurante.py`**, **`supermercado.py`**, **`farmacia.py`**: Definen las clases específicas para cada tipo de tienda, heredando de `Tienda`.

## Clases y Métodos

### Clase `Tienda`

#### Atributos

- **`nombre`**: Nombre de la tienda.
- **`costo_delivery`**: Costo de entrega asociado a la tienda.
- **`productos`**: Lista de productos disponibles en la tienda.

#### Métodos

- **`ingresar_producto(producto)`**: Agrega un producto a la tienda. Si el producto ya existe, suma el stock del nuevo ingreso al stock existente.
- **`listar_productos()`**: Método abstracto que debe ser implementado por cada tipo específico de tienda para listar sus productos.
- **`realizar_venta(nombre_producto, cantidad)`**: Método abstracto que debe ser implementado por cada tipo específico de tienda para realizar una venta.

### Clase `Producto`

#### Atributos

- **`nombre`**: Nombre del producto.
- **`precio`**: Precio del producto.
- **`stock`**: Stock disponible del producto.

#### Métodos

- **`modificar_stock(cantidad)`**: Modifica el stock sumando o restando una cantidad determinada.
- **`__eq__(self, other)`**: Compara dos productos para ver si son iguales en su nombre.

## Función Principal (`main` en `programa.py`)

La función principal maneja la interacción del usuario, permitiendo:

- Crear una tienda.
- Ingresar productos.
- Listar productos.
- Realizar ventas.
- Salir del programa.

## Ejecución del Programa

Para ejecutar el programa, simplemente corre el archivo `programa.py`:

```bash
python programa.py
```
## Instalación

1. Clone el repositorio:

```bash
git clone https://github.com/curso-python-g20-grupo5/Interacciones-entre-objetos.git
```

2. Navegue al directorio del proyecto:

```bash
cd interacciones-entre-objetos
```

3. Ejecute los scripts según las instrucciones en la sección de Ejecución del Programa.

## Contribución

Si desea contribuir a este proyecto, por favor haga un fork del repositorio y envíe un pull request con sus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo `LICENSE` para obtener más detalles.

---

## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)

⌨️ con ❤️ por el Grupo 5 - G20 😊