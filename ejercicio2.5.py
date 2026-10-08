from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    def __init__(self, nombres_titular: str, apellidos_titular: str, 
                 numero_cuenta: str, tipo_cuenta: TipoCuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta bancaria = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.value}")
        print(f"Saldo de la cuenta = ${self.saldo:.2f}\n")

    def consultar_saldo(self):
        print(f"El saldo actual de la cuenta es = ${self.saldo:.2f}")

    def consignar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            print(f"Se consigó el valor de ${valor:.2f} a la cuenta. Nuevo saldo = ${self.saldo:.2f}")
        else:
            print("El valor a consignar debe ser mayor que cero.")

    def retirar(self, valor: float):
        if valor <= 0:
            print("El valor a retirar debe ser mayor que cero.")
        elif valor > self.saldo:
            print(f"No se puede realizar el retiro de ${valor:.2f}. El valor solicitado supera el saldo actual (${self.saldo:.2f}).")
        else:
            self.saldo -= valor
            print(f"Se retiró el valor de ${valor:.2f} de la cuenta. Nuevo saldo = ${self.saldo:.2f}")

def main():
    cuenta = CuentaBancaria("Mateo", "Morales", "987654321", TipoCuenta.CORRIENTE)
    cuenta.imprimir()

    cuenta.consignar(300000)
    cuenta.consignar(150000)
    cuenta.retirar(80000)
    cuenta.retirar(500000)

if __name__ == "__main__":
    main()