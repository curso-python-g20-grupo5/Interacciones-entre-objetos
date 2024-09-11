class Tienda:
    """
    Clase base que representa una tienda genérica.

    Atributos:
        nombre (str): El nombre de la tienda.
        costo_delivery (float): El costo de entrega asociado a la tienda.
        productos (list): Lista de productos disponibles en la tienda.

    Métodos:
        ingresar_producto(producto):
            Agrega un producto a la tienda. Si el producto ya existe, suma el stock del nuevo ingreso al stock existente.

        listar_productos():
            Método abstracto que debe ser implementado por cada tipo específico de tienda para listar sus productos.

        realizar_venta(nombre_producto, cantidad):
            Método abstracto que debe ser implementado por cada tipo específico de tienda para realizar una venta.
    """

    def __init__(self, nombre, costo_delivery):
        """
        Inicializa una instancia de la clase Tienda.

        Args:
            nombre (str): El nombre de la tienda.
            costo_delivery (float): El costo de entrega asociado a la tienda.
        """
        self.nombre = nombre
        self.costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, producto):
        """
        Agrega un producto a la tienda. Si el producto ya existe, suma el stock del nuevo ingreso al stock existente.

        Args:
            producto (Producto): El producto a ingresar.
        """
        for p in self.productos:
            if p == producto:
                p + producto.stock  # Suma el stock del nuevo ingreso
                return
        self.productos.append(producto)


class Restaurante(Tienda):
    """
    Clase que representa un restaurante, hereda de Tienda.

    Methods:
        ingresar_producto(producto):
            Agrega un producto al restaurante con stock siempre igual a 0.

        listar_productos():
            Lista los productos disponibles en el restaurante.

        realizar_venta(nombre_producto, cantidad):
            Realiza una venta de un producto en el restaurante.
    """

    def ingresar_producto(self, producto):
        """
        Agrega un producto al restaurante con stock siempre igual a 0.

        Args:
            producto (Producto): El producto a ingresar.
        """
        producto.stock = 0  # Siempre 0 para Restaurante
        super().ingresar_producto(producto)

    def listar_productos(self):
        """
        Lista los productos disponibles en el restaurante.

        Returns:
            str: Una cadena con la lista de productos.
        """
        return "\n".join(
            [f"Producto: {p.nombre}, Precio: ${p.precio}" for p in self.productos]
        )

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Realiza una venta de un producto en el restaurante.

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad a vender.
        """
        for p in self.productos:
            if p.nombre == nombre_producto:
                print(f"Venta realizada: {cantidad} de {nombre_producto}")
                return
        print(f"Producto {nombre_producto} no encontrado.")


class Supermercado(Tienda):
    """
    Clase que representa un supermercado, hereda de Tienda.

    Methods:
        listar_productos():
            Lista los productos disponibles en el supermercado.

        realizar_venta(nombre_producto, cantidad):
            Realiza una venta de un producto en el supermercado.
    """

    def listar_productos(self):
        """
        Lista los productos disponibles en el supermercado.

        Returns:
            str: Una cadena con la lista de productos.
        """
        resultado = []
        for p in self.productos:
            stock_msg = f"{p.stock} unidades"
            if p.stock < 10:
                stock_msg += " - Pocos productos disponibles"
            resultado.append(
                f"Producto: {p.nombre}, Precio: ${p.precio}, Stock: {stock_msg}"
            )
        return "\n".join(resultado)

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Realiza una venta de un producto en el supermercado.

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad a vender.
        """
        for p in self.productos:
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p - cantidad
                else:
                    cantidad = p.stock
                    p.stock = 0
                print(f"Venta realizada: {cantidad} de {nombre_producto}")
                return
        print(f"Producto {nombre_producto} no encontrado o sin stock.")


class Farmacia(Tienda):
    """
    Clase que representa una farmacia, hereda de Tienda.

    Methods:
        listar_productos():
            Lista los productos disponibles en la farmacia.

        realizar_venta(nombre_producto, cantidad):
            Realiza una venta de un producto en la farmacia.
    """

    def listar_productos(self):
        """
        Lista los productos disponibles en la farmacia.

        Returns:
            str: Una cadena con la lista de productos.
        """
        resultado = []
        for p in self.productos:
            envio_gratis = ", Envío gratis" if p.precio > 15000 else ""
            resultado.append(f"Producto: {p.nombre}, Precio: ${p.precio}{envio_gratis}")
        return "\n".join(resultado)

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Realiza una venta de un producto en la farmacia.

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad a vender.
        """
        if cantidad > 3:
            print("No se puede solicitar más de 3 unidades por producto.")
            return
        for p in self.productos:
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p - cantidad
                else:
                    cantidad = p.stock
                    p.stock = 0
                print(f"Venta realizada: {cantidad} de {nombre_producto}")
                return
        print(f"Producto {nombre_producto} no encontrado o sin stock.")
