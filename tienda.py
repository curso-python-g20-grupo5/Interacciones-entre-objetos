class Tienda:
    """
    Clase base que representa una tienda genérica.

    Atributos:
    ----------
    nombre : str
        El nombre de la tienda.
    costo_delivery : float
        El costo de entrega asociado a la tienda.
    productos : list
        Lista de productos disponibles en la tienda.

    Métodos:
    --------
    ingresar_producto(producto):
        Agrega un producto a la tienda. Si el producto ya existe, suma el stock del nuevo ingreso al stock existente.
    
    listar_productos():
        Método abstracto que debe ser implementado por cada tipo específico de tienda para listar sus productos.

    realizar_venta(nombre_producto, cantidad):
        Método abstracto que debe ser implementado por cada tipo específico de tienda para realizar una venta.
    """
    def __init__(self, nombre, costo_delivery):
        self.nombre = nombre
        self.costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, producto):
        for p in self.productos:
            if p == producto:
                p + producto.stock  # Suma el stock del nuevo ingreso
                return
        self.productos.append(producto)

    def listar_productos(self):
        raise NotImplementedError(
            "Este método debe ser implementado por cada tipo de tienda."
        )

    def realizar_venta(self, nombre_producto, cantidad):
        raise NotImplementedError(
            "Este método debe ser implementado por cada tipo de tienda."
        )