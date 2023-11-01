dados_clinte = {
 "Nome":"Gustavo",
 "Endereço":"Rua ABC, 123",
 "Telefone": "9999999999"
 }

print (dados_clinte['Nome'])

dados_clinte['cidade'] = "Ivaipora" #Adiciona mais um topico no adicionario

print (dados_clinte)

dados_clinte.pop('Telefone') #Remove um topico do Dicionario.

print (dados_clinte)

for indice , valor in dados_clinte.items():

    print(f'indice:{indice}, valor: {valor}')

    print ('::::::::::::::::::::::::::::::::')