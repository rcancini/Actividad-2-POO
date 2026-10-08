import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return (2 * self.base) + (2 * self.altura)


class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:
        h = self.calcular_hipotenusa()
        if self.base == self.altura and self.base == h:
            return "Equilátero"
        elif self.base != self.altura and self.base != h and self.altura != h:
            return "Escaleno"
        else:
            return "Isósceles"

def main():
    figura1 = Circulo(4.5)
    figura2 = Rectangulo(6.0, 3.0)
    figura3 = Cuadrado(5.0)
    figura4 = TrianguloRectangulo(6.0, 8.0)

    print(f"El área del círculo es = {figura1.calcular_area():.2f}")
    print(f"El perímetro del círculo es = {figura1.calcular_perimetro():.2f}\n")

    print(f"El área del rectángulo es = {figura2.calcular_area():.2f}")
    print(f"El perímetro del rectángulo es = {figura2.calcular_perimetro():.2f}\n")

    print(f"El área del cuadrado es = {figura3.calcular_area():.2f}")
    print(f"El perímetro del cuadrado es = {figura3.calcular_perimetro():.2f}\n")

    print(f"El área del triángulo es = {figura4.calcular_area():.2f}")
    print(f"El perímetro del triángulo es = {figura4.calcular_perimetro():.2f}")
    print(f"La hipotenusa del triángulo es = {figura4.calcular_hipotenusa():.2f}")
    print(f"El tipo de triángulo es = {figura4.determinar_tipo_triangulo()}")

if __name__ == "__main__":
    main()