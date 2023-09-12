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

    def __str__(self):
        return f"{self.nome} - Fome: {self.fome}, Tédio: {self.tedio}"

if __name__ == "__main__":
    charmander = "Charizard"
    pokemon = Pokemon(charmander)

    while True:
        print("\nMenu:")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Mostrar Status")
        print("4. Opção Secreta (Mostrar Atributos Exatos)")
        print("5. Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            comida = int(input("Quantidade de comida fornecida (0-100): "))
            pokemon.alimentar(comida)
        elif escolha == 2:
            brincadeira = int(input("Tempo de brincadeira (0-100): "))
            pokemon.brincar(brincadeira)
        elif escolha == 3:
            pokemon.mostrar_status()
        elif escolha == 4:
            senha = input("Digite a senha secreta: ")
            if senha == "1234":
                print(pokemon)
            else:
                print("Senha incorreta!")
        elif escolha == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")
