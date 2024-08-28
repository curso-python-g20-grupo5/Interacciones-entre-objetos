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

#se define el método modificar_stock, el cual modifica el stock sumando o restando una catidad determinada
    def modificar_stock(self, cantidad):
        self.__stock = max(0, self.__stock + cantidad) #se ingresa un stock 0 como valor mínimo ya que el stock no puede ser negativo

    def __eq__(self, other):
        return self.__nombre == other.nombre #se comparan dos productos para ver si son iguales en su nombre
