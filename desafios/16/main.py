class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    

    def apresentação(self):
        return f'ola, sou {self.nome} e sou {self.cargo} do setor {self.setor}'





rr = Funcionario("pedro", "adm", "diretor")
print(rr.apresentação())


r2 = Funcionario('juana', 'atendimento', 'atendente')
print(r2.apresentação())
