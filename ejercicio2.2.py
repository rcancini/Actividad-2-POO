from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre: str, cantidad_satelites: int, masa: float, 
                 volumen: float, diametro: int, distancia_sol: int, 
                 tipo: TipoPlaneta, es_observable: bool):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self) -> float:
        return self.masa / self.volumen if self.volumen != 0 else 0.0

    def es_planeta_exterior(self) -> bool:

        limite_exterior = 149597870 * 3.4
        return self.distancia_sol > limite_exterior

def main():
    
    p1 = Planeta("Marte", 2, 6.4171e23, 1.6318e11, 6779, 228, TipoPlaneta.TERRESTRE, True)
    
    p2 = Planeta("Neptuno", 14, 1.024e26, 6.254e13, 49244, 4495, TipoPlaneta.GASEOSO, False)

    print("--- PLANETA 1 ---")
    p1.imprimir()
    print(f"Densidad = {p1.calcular_densidad():.2f}")
    print(f"Es planeta exterior = {p1.es_planeta_exterior()}\n")

    print("--- PLANETA 2 ---")
    p2.imprimir()
    print(f"Densidad = {p2.calcular_densidad():.2f}")
    print(f"Es planeta exterior = {p2.es_planeta_exterior()}\n")

if __name__ == "__main__":
    main()