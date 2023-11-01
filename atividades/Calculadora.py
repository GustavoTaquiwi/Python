numero01 = input('Digite o primeiro número:\n')

try:
    numero01_float = float(numero01)
except:
    print('Seus dados estão incorretos!')
    exit()

operador = input('Digite o operador para o calculo (+-*/)\n')
numero02 = input('Digite o segundo número:\n')

try:
    numero02_float = float(numero02)
except:
    print('Seus dados estão incorretos!')
    exit()

if operador == '+':
    resultado = numero01_float + numero02_float
    print(f'A soma entre {numero01_float} e {numero02_float} é: {resultado}')
elif operador == '-':
    resultado = numero01_float - numero02_float
    print(f'A subtração entre {numero01_float} e {numero02_float} é: {resultado}')
elif operador == '*':
    resultado = numero01_float * numero02_float
    print(f'A multiplicação entre {numero01_float} e {numero02_float} é: {resultado}')
elif operador == '/':
    resultado = numero01_float / numero02_float
    print(f'A divisão entre {numero01_float} e {numero02_float} é: {resultado}')
elif operador != '+' or '*' or '/' or '-':
    print('O seu operador é inválido.')