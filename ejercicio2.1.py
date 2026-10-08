class Persona:
    def __init__(self, nombre: str, apellido: str, numero_documento: str, ano_nacimiento: int):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.ano_nacimiento = ano_nacimiento

    def imprimir(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellido = {self.apellido}")
        print(f"Número de documento de identidad = {self.numero_documento}")
        print(f"Año de nacimiento = {self.ano_nacimiento}")
        print()

def main():
    persona1 = Persona("Santiago", "Gómez", "1017215890", 2002)
    persona2 = Persona("Valentina", "Ríos", "1028394102", 2004)

    persona1.imprimir()
    persona2.imprimir()

if __name__ == "__main__":
    main()