# producto.py
# Método constructor de la clase. Se instancia la clase producto y se le asigna un nombre, un precio y un stock inicial
# el stock se inicia en 0. Si el valor de un stock es negativo, este se ajusta al valor 0 puesto que el stock no puede ser negativo
class Producto:
    """Clase que representa un producto con nombre, precio y stock.

    Attributes:
        nombre (str): El nombre del producto.
        precio (float): El precio del producto.
        stock (int): El stock del producto, no puede ser negativo.

    """

    def __init__(self, nombre, precio, stock=0):
        """Inicializa una instancia de la clase Producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
            stock (int, optional): El stock inicial del producto. Default es 0. Si es negativo, se ajusta a 0.

        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)  # Stock no puede ser negativo

    # se ocupa property para poder acceder a las propiedades de los atributos privados de manera controlada
    @property
    def nombre(self):
        """str: Obtiene el nombre del producto."""
        return self.__nombre

    @property
    def precio(self):
        """float: Obtiene el precio del producto."""
        return self.__precio

    @property
    def stock(self):
        """int: Obtiene el stock del producto."""
        return self.__stock

    @stock.setter
    def stock(self, valor):
        """Establece el stock del producto.

        Args:
            valor (int): El nuevo valor del stock. Si es negativo, se ajusta a 0.

        """
        self.__stock = max(0, valor)

    def __add__(self, cantidad):
        """Incrementa el stock del producto.

        Args:
            cantidad (int): La cantidad a incrementar en el stock.

        Returns:
            Producto: La instancia actual del producto con el stock actualizado.

        """
        self.stock += cantidad
        return self

    def __sub__(self, cantidad):
        """Decrementa el stock del producto.

        Args:
            cantidad (int): La cantidad a decrementar en el stock.

        Returns:
            Producto: La instancia actual del producto con el stock actualizado.

        """
        self.stock = max(0, self.stock - cantidad)
        return self

    def __eq__(self, otro):
        """Compara si dos productos son iguales basándose en su nombre.

        Args:
            otro (Producto): El otro producto a comparar.

        Returns:
            bool: True si los nombres de los productos son iguales, False en caso contrario.

        """
        if isinstance(otro, Producto):
            return self.nombre == otro.nombre
        return False
