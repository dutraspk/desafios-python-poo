


class Churrasco():
    def __init__(self, titulo='', quantidade=0):
        self.ti = titulo
        self.quan = quantidade
        #400 grama por pessoa e R$82.40 por Kg de carne
    
    def linha(self):
        return '-'*40
    

    def contaKG(self):
        
        return  self.quan * 0.4
        #400g por pessoa

    def contavalortotaldecarne(self):
        a = 82.40
        contatotal = self.contaKG() * a
        #R$82.40 por Kg
        return  contatotal
    
    def contaporpessoa(self):
        return self.contavalortotaldecarne() / self.quan
    

    def analise(self):
        print(self.linha())
        print(f'recomendo comprar {self.contaKG():.3f}Kg de carne')
        print(f'O custo total sera de R${self.contavalortotaldecarne():.2f}')
        print(f'Cada pessoa pagara R${self.contaporpessoa():.2f}')
        return



c1 = Churrasco('pipoka', 15)
c1.analise()