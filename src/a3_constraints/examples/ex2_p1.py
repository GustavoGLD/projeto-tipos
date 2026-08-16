"""
CRIANDO UMA CONSTRAINT

Só é possível conversar com seres vivos que falam (objetos com metodo `conversar()`)
Não é posssível conversar com cachorros, eles latem! (objetos sem o metodo `conversar()`)

Podemos comparar nossa situação a constraints:
    - Adulto e Bebê respondem a Constraint `SerVivoFalante`
    - Cachorro e demais tipos, não.

A regra para participar da Constraint `SerVivoFalante` é ter um metodo `conversar()`
"""

from typing import Protocol

class SerVivoFalante(Protocol):
    def conversar(self) -> None: ...

class Adulto:
    def conversar(self):
        print("Boa tarde!")

class Bebe:
    def conversar(self):
        print("gugu dadá!")

class Cachorro:
    def latir(self):
        print("au au au!")

def conversar_com(ser_vivo: SerVivoFalante) -> None:
    ser_vivo.conversar()

if __name__ == "__main__":
    pessoa = Adulto()
    bebe = Bebe()
    cachorro = Cachorro()
    conversar_com(pessoa)    # isso dá certo
    conversar_com(bebe)      # isso também dá certo
    conversar_com(cachorro)  # mas isso dá erro