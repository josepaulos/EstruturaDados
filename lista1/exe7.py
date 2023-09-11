class pokemon:
    def __init__(self,nome,fome,saude,idadeP):
        self.nome=nome
        self.fome=fome
        self.saude=saude
        self.idadeP=idadeP
        return print('Nome',self.nome,'Fome',self.fome,'Saude',self.saude,'Level',self.idadeP)

    def Evoluir(self,nomeI):
        self.nome=nomeI
        return self.nome
    
    def Humor(self):
        humor = (self.fome + self.saude) / 2
        if humor > 50:
            print(f'O humor de {self.nome} está em {humor:.0f}% e ele está feliz e animado.')
        else:
            print(f'O humor de {self.nome} está em {humor:.0f}% e ele está triste e com fome.')
    
    def Level(self,taficandovelho):
        self.idadeP=taficandovelho
        return self.idadeP
    
    def Quemeessepoquemon(self):
        return print('Nome',self.nome,'Fome',self.fome,'Saude',self.saude,'Level',self.idadeP)
    



charmander=pokemon('Charmander',10,100,10)
print(charmander.Evoluir('Charizard'))
print(charmander.Level(36))
charmander.Humor()
charmander.Quemeessepoquemon()
