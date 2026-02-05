

class Produto:
    def __init__(self, nome = '', preço = 0):
        self.nome = nome
        self.preço = preço
    
    def etiqueta(self):
        print(f'{self.nome:^30}\n{'-'*30}\n{self.preço:_^30.2f}')
        return 
    

c1 = Produto('memória ram 8gb ddr3', 690)
c1.etiqueta()