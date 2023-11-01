
numeros = []


for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)


soma = 0
for num in numeros:
    soma += num


print("Números digitados:", numeros)
print("Soma dos valores:", soma)
