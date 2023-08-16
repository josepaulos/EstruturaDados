class Automovel:
    def __init__(self, placa , nome, cor):
        self.placa = placa
        self.nome = nome
        self.cor = cor
    def get_placa(self):
        return print('a placa é ',self.placa)
    def get_nome(self):
        return print('o nome é ',self.nome)
    def get_cor(self):
        return print('A cor é ', self.cor)
    def get_td(self):
        return print('a placa é ',self.placa), print('o nome é ',self.nome), print('A cor é ', self.cor)
    def dirigir(self, velocidade):
        print('Estou com o carro',self.nome,'da cor ',self.cor,'da placa',self.placa, 'dirigindo a',velocidade,'km/h' )

class Pessoa:
    def __init__(self,nome='José Paulo', idade='22', altura='180'):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def get_pessoa(self):
        return print('meu nome é',self.nome,'minha idade é',self.idade,'e o tamanho da minha altura ',self.altura)

celta = Automovel('123123','celta','rosa')

celta.get_placa()
celta.get_nome()
celta.get_cor()
celta.dirigir(69)

palio = Automovel('321321', 'palio','roxo')
palio.get_td()
palio.dirigir(60)

tucson = Automovel('6565','Tucson','preto')
tucson.get_td()
tucson.dirigir(100)

jose = Pessoa()
jose.get_pessoa()


