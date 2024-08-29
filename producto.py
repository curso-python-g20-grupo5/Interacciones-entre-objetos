#producto.py
#Método constructor de la clase. Se instancia la clase producto y se le asigna un nombre, un precio y un stock inicial
#el stock se inicia en 0. Si el valor de un stock es negativo, este se ajusta al valor 0 puesto que el stock no puede ser negativo
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)  # Stock no puede ser negativo

#se ocupa property para poder acceder a las propiedades de los atributos privados de manera controlada
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        self.__stock = max(0, valor)

    def __add__(self, cantidad):
        self.stock += cantidad
        return self

    def __sub__(self, cantidad):
        self.stock = max(0, self.stock - cantidad)
        return self

    def __eq__(self, otro):
        if isinstance(otro, Producto):
            return self.nombre == otro.nombre
        return False
