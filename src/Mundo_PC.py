
class DispositivoEntrada:

    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    def __str__(self):
        return f"Tipo de entrada: {self._tipo_entrada}, Marca: {self._marca}"

    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca


class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        self._id = self.obtener_id()

    @classmethod
    def obtener_id(cls):
        cls.contador_ratones += 1
        return cls.contador_ratones

    def __str__(self):
        return f"Id: {self._id}, {super().__str__()}"


class Teclado(DispositivoEntrada):

    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        self._id = self.obtener_id()

    @classmethod
    def obtener_id(cls):
        cls.contador_teclados += 1
        return cls.contador_teclados

    def __str__(self):
        return f"Id: {self._id}, {super().__str__()} "


class Monitor:

    contador_monitores = 0

    @classmethod
    def incrementar_valor(cls):
        cls.contador_monitores += 1
        return cls.contador_monitores

    def __init__(self, marca, tamanio):
        self._marca = marca
        self._tamanio = tamanio
        self._id = self.incrementar_valor()

    @property
    def tamanio(self):
        return self._marca

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @classmethod
    def cantidad(cls):
        return cls.contador_monitores

    def __str__(self):
        return f"Monitor {self._id}: {self._marca}, Tamaño: {self._tamanio}"


class Computadora:

    cantidad_computadoras = 0

    @classmethod
    def incrementar_valor(cls):
        cls.cantidad_computadoras += 1
        return cls.cantidad_computadoras

    def __init__(self, nombre, monitor, teclado, raton):
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        self._id = self.incrementar_valor()


    def __str__(self):
        return f"""
        {self._nombre}: {self._id}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        """

class Orden:

    contador_ordenes = 0

    @classmethod
    def incrementar_valor(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, computadora, ):
        self._computadoras = computadora

        self._id = self.incrementar_valor()

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f"""
        Orden: {self._id}
        Computadoras: {computadoras_str}
        
        """


if __name__ == "__main__":
    teclado1 = Teclado("USB", "HP")
    raton1 = Raton("USB", "HP")
    monitor1 = Monitor("HP", 15)
    computadora1 = Computadora("HP", monitor1, teclado1, raton1)
    teclado2 = Teclado("USB", "Lenovo")
    raton2 = Raton("BT", "Redragon")
    monitor2 = Monitor("Philips", 23)
    computadora2 = Computadora("Thermaltake", monitor2, teclado2, raton2)

    computadoras1 = [computadora1, computadora2]
    #print(computadora1)
    orden1 = Orden(computadoras1)
    print(orden1)
