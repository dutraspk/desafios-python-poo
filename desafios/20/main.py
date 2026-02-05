class Gamer:
    def __init__(self, nome='', nick=''):
        self.nome = nome
        self.nick = nick
    

    def add_favorito(self, game=''):
        a = game
        print(a)
        return a
    
    def linha(self):
        return print('-'*30)
    

    def ficha(self):
        self.linha()
        print(f'nome real: {self.nome}')
        self.linha()
        print('Jogos favoritos:')
        for i in self.add_favorito():
            print(i)

        return
    

g1 = Gamer('pedro', 'prefa')
g1.add_favorito('pedra')
g1.add_favorito('cod')


g1.ficha()
