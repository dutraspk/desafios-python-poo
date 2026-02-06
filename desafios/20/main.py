class Gamer:
    def __init__(self, nome='', nick=''):
        self.nome = nome
        self.nick = nick
     
    def linha(self):
        return print('-'*30)


    def add_favorito(self, game=''):
            
            return print(game)

    def ficha(self):
        self.linha()
        print(f'nome real: {self.nome}')
        self.linha()
        print('Jogos favoritos:')
        
        self.add_favorito()
        return  
    
    

    

g1 = Gamer('pedro', 'prefa')
g1.add_favorito('pedra')

g1.add_favorito('cod')

g1.ficha()

