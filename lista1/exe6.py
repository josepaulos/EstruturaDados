class Televisor:
    def __init__(self):
        self.canal = 1 
        self.volume = 10  

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:  
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal inválido")

    def aumentar_volume(self):
        if self.volume < 100: 
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")

    def diminuir_volume(self):
        if self.volume > 0:  
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")



tv = Televisor()

while True:
    print("\nControle Remoto do Televisor")
    print("1 - Mudar de Canal")
    print("2 - Aumentar Volume")
    print("3 - Diminuir Volume")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        novo_canal = int(input("Digite o número do canal: "))
        tv.mudar_canal(novo_canal)
    elif opcao == 2:
        tv.aumentar_volume()
    elif opcao == 3:
        tv.diminuir_volume()
    elif opcao == 4:
        print("Desligando o televisor.")
        break
    else:
        print("Opção inválida. Tente novamente.")
