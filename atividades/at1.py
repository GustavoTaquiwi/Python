nome = str(input ('Qual seu Nome?'))
sbnome = str(input ('Qual seu sobre nome?'))
idade = int(input ('Qual sua Idade?'))
altura = float(input ('Qual sua altura?'))         
peso = float(input ('Qual seu peso?'))
print ('{},{},{},{},{},\n'.format(nome,sbnome,idade,altura,peso))

if idade > 18:
       
    print ('Vc e maior de idade!!')

else:

    print ('Vc e menor de idade!!')
