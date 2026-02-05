
class Livro():
    def __init__(self, titulo='',paginas=1):
        self.ti = titulo
        self.pag = paginas
        self.npag = 1
        print(f'Você acabou de abrir o livro "{self.ti}" que tem {self.pag} páginas no total. Você agora está na página {self.npag}')

    def avançarpagina(self, pagpass):
        if pagpass > self.pag - self.npag:
            pagpass = self.pag - self.npag
    
        for i in range(self.npag + 1, self.npag + pagpass + 1):
            print(f'pág{i} → ', end='')

        
        self.npag += pagpass

        if self.npag == self.pag and pagpass == 0:
            print(f'Você chegou ao final do livro "{self.ti}"')
        else:
            print(f'Você avançou {pagpass} páginas e agora está na página {self.npag}')
        

        return

l1 = Livro('o pequeno princepe', 20)
l1.avançarpagina(15)
l1.avançarpagina(1)
l1.avançarpagina(20)