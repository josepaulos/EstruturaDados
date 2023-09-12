class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def definir_ponto(self, xN, yN):
        self.x = xN
        self.y = yN

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.largura / 2
        centro_y = self.altura / 2
        return Ponto(centro_x, centro_y)


pontinho = Ponto(3,4)
retangulo = Retangulo(largura=10, altura=6)


retanguloC = retangulo.encontrar_centro()


print(f"Valores do ponto: x={pontinho.x}, y={pontinho.y}")
print(f"Centro do retângulo: x={retanguloC.x}, y={retanguloC.y}")


pontinho.definir_ponto(5, 7)


retanguloC2 = retangulo.encontrar_centro()


print(f"Novos valores do ponto: x={pontinho.x}, y={pontinho.y}")
print(f"Centro do retângulo após a mudança: x={retanguloC2.x}, y={retanguloC2.y}")