from typing import Type
from formas_interface import FormasInterface

class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]):
        perimetro = terreno.get_perimetro()
        print(f'{self.nome} mediu o perimetro: {perimetro} m')

    def medir_area(self, terreno: Type[FormasInterface]):
        area = terreno.get_area()
        print(f'{self.nome} mediu a area: {area} m2')