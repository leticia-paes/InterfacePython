from quadrado import TerrenoQuadrado
from retangulo import TerrenoRetangular
from engenheiro import Engenheiro

engenheiro = Engenheiro('Geraldo')
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangular(2,3)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_area(terrenoRetangular)

engenheiro.medir_perimetro(terrenoQuadrado)
engenheiro.medir_perimetro(terrenoRetangular)
