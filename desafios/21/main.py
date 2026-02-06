class Caneta:
    def __init__(self, cor='\033[37m'):
        self.cor = cor
        self.cor.strip().lower()
        if self.cor == 'verde':
            self.cor = '\033[32m'

        elif self.cor == 'rosa':
            self.cor = '\033[35m'



    def destampar(self,ver=False):
        print(ver)
        return 

    def escrever(self, escrever):
        if self.destampar() == True:
            print(f'{self.cor}{escrever}\033m')
        else:
            print('vc precisa destampar a caneta')
        return
    
    def quebrar_linha(self,quantidade=0):
        
        for i in range(0,quantidade):
            print('')







c1 = Caneta('verde')
c1.destampar(True)
c1.quebrar_linha(1)
c1.escrever('aaaaaaaa')
c2 = Caneta('rosa')
c2.escrever('sssssss')