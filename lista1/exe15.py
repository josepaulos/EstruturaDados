class Pokemon:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50  
        self.tedio = 50  

    def alimentar(self, quantidade_bary):
       
        self.fome -= quantidade_bary
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_de_brincadeira):
      
        self.tedio -= tempo_de_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        if self.fome >= 70 and self.tedio >= 70:
            return "Muito mal-humorado"
        elif self.fome >= 70:
            return "Mal-humorado"
        elif self.tedio >= 70:
            return "Entediado"
        else:
            return "Feliz"

    def mostrar_status(self):
        print(f"{self.nome} está se sentindo {self.humor()}.")
        print(f"Nível de Fome: {self.fome}")
        print(f"Nível de Tédio: {self.tedio}")


charmander = "Charizard"
pokemon = Pokemon(charmander)

print("\nStatus Inicial do pokemon:")
pokemon.mostrar_status()

bary = int(input("Quantidade de bary fornecida (0-100): "))
brincadeira = int(input("Tempo de brincadeira (0-100): "))

pokemon.alimentar(bary)
pokemon.brincar(brincadeira)

print("\nStatus Atual do pokemon:")
pokemon.mostrar_status()