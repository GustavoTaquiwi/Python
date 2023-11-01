class Universidade:
    def __init__(self, nome):
        self.nome = nome
    
    def possui(self, curso):
        print(f'A {self.nome} possui o curso de {curso.nome}')

class Curso:
    def __init__(self, nome):
        self.nome = nome
    
    def professor(self, professor):
        print(f'O nome do professor do curso de {self.nome} é {professor.nome}')

class Professor:
    def __init__(self, nome):
        self.nome = nome
    
    def trabalha(self, universidade):
        print(f'O professor {self.nome} trabalha na {universidade.nome}')

universidade1 = Universidade('Univale')
curso1 = Curso('Análise e Desenvolvimento de Sistemas')
professor1 = Professor('Dieimis')

universidade1.possui(curso1)
curso1.professor(professor1)
professor1.trabalha(universidade1)