def limpartela():
    import os
    os.system("cls")

limpartela()
print ('Boa noite Estudante!')

################################################################################################################

def soma (num1, num2):
    print (num1 + num2)
num1 = 2
num2 = 3
soma (num1, num2)

####################################################################################################################

def soma2 (numero11, numero2):
   return numero11 + numero2

resultado = soma2 (3,3)
print(resultado)

#####################################################################################################################

def exemplo(a,b,c):
    print (a, b, c)

exemplo(1,2,3)    

#########################################################################################################################

def exemplo(a, b, c):
    print(a, b, c)

exemplo (a=1, b=3, c=2)

####################################################################################################################

def exemplo(a, b=2, c=3):
    print(a, b, c)
exemplo(1)

exemplo(1, c = 5)

############################################################################################################################

def minha_funcao(*args):
    for arg in args:
        print(arg)
    print(type(args))

minha_funcao(1, 2, 3, 4)        

####################################################################################################################

def minha_funcao (**kwargs):
    for chave, valor in kwargs.items():
        print(f'A Chave é {chave} e o valor é {valor}')
    print(type(kwargs))


minha_funcao(nome="joao", idade=25, pais="brasil") 

###############################################################################################################

def minha_funcao():
    return "Funçao do Modulo"
if __name__=="__main__":
   print(' Este Script esta sendo executao sozinho')
else:
    print('Este Scripth foi Importado')  

###########################################################################################################################    

def soma (x:float , y: float):
    return x + y 
 

###########################################################################################################################

class carro:
    pneus = 4

    def __init__(self, marca , modelo):
        self.marca = marca
        self.modelo = modelo

############################################################################################################################

class turma:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def texto(self):
        print (f"O Meu Nome é {self.nome} e meu sobrenome é {self.sobrenome}")

aluno1 = turma("Gustavo", "Ariosi")
print(aluno1.nome)
print(aluno1.sobrenome)

aluno1.texto()
   
