from enum import Enum

class TipoCom(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class TipoA(Enum):
    CIUDAD = "Carro de Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    def __init__(self, marca: str, modelo: int, motor: float, 
                 tipo_combustible: TipoCom, tipo_automovil: TipoA, 
                 numero_puertas: int, cantidad_asientos: int, 
                 velocidad_maxima: float, color: TipoColor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0.0

    # Getters y Setters
    def get_marca(self): return self.marca
    def set_marca(self, marca): self.marca = marca

    def get_modelo(self): return self.modelo
    def set_modelo(self, modelo): self.modelo = modelo

    def get_motor(self): return self.motor
    def set_motor(self, motor): self.motor = motor

    def get_tipo_combustible(self): return self.tipo_combustible
    def set_tipo_combustible(self, tipo): self.tipo_combustible = tipo

    def get_tipo_automovil(self): return self.tipo_automovil
    def set_tipo_automovil(self, tipo): self.tipo_automovil = tipo

    def get_numero_puertas(self): return self.numero_puertas
    def set_numero_puertas(self, num): self.numero_puertas = num

    def get_cantidad_asientos(self): return self.cantidad_asientos
    def set_cantidad_asientos(self, cant): self.cantidad_asientos = cant

    def get_velocidad_maxima(self): return self.velocidad_maxima
    def set_velocidad_maxima(self, vel): self.velocidad_maxima = vel

    def get_color(self): return self.color
    def set_color(self, color): self.color = color

    def get_velocidad_actual(self): return self.velocidad_actual
    def set_velocidad_actual(self, vel): self.velocidad_actual = vel

    # Métodos de control
    def acelerar(self, incremento: float):
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            print(f"No se puede acelerar a {self.velocidad_actual + incremento} km/h. Supera la velocidad máxima permitida ({self.velocidad_maxima} km/h).")
        else:
            self.velocidad_actual += incremento

    def desacelerar(self, decremento: float):
        if self.velocidad_actual - decremento < 0:
            print("No se puede desacelerar a una velocidad negativa.")
        else:
            self.velocidad_actual -= decremento

    def frenar(self):
        self.velocidad_actual = 0.0

    def calcular_tiempo_llegada(self, distancia: float) -> float:
        if self.velocidad_actual == 0:
            return float('inf')
        return distancia / self.velocidad_actual

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor} L")
        print(f"Tipo de combustible = {self.tipo_combustible.value}")
        print(f"Tipo de automóvil = {self.tipo_automovil.value}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima} km/h")
        print(f"Color = {self.color.value}")
        print(f"Velocidad actual = {self.velocidad_actual} km/h")

def main():
    auto = Automovil("Mazda", 2022, 2.0, TipoCom.GASOLINA, TipoA.COMPACTO, 4, 5, 210.0, TipoColor.ROJO)
    auto.imprimir()

    print("\n--- Pruebas de Velocidad ---")
    auto.set_velocidad_actual(80.0)
    print(f"Velocidad inicial: {auto.get_velocidad_actual()} km/h")

    auto.acelerar(30.0)
    print(f"Velocidad tras acelerar 30 km/h: {auto.get_velocidad_actual()} km/h")

    auto.desacelerar(40.0)
    print(f"Velocidad tras desacelerar 40 km/h: {auto.get_velocidad_actual()} km/h")

    auto.frenar()
    print(f"Velocidad tras frenar: {auto.get_velocidad_actual()} km/h")

if __name__ == "__main__":
    main()