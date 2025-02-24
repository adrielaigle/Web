#Questão 1
'''Escreva um programa que imprime todos os numeros de 0 até 50, incluindo-os.

c = 1
while c < 51:
    print(c)
    c = c + 1
print("Acabou.")'''

#Questão 2
'''Modifique o programa anterior de forma que este imprima apenas os
números que são pares.

c = 2
while c < 51:
    print(c)
    c = c + 2
print("Acabou.")'''

#Questão 3
'''Escreva um programa para contar a quantidade de números pares entre dois
números quaisquer fornecidos pelo usuário.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
contador = 0 
numero = num1 
while numero <= num2:
    if numero % 2 == 0:
        contador += 1
    numero += 1 
print(f"A quantidade de números pares entre {num1} e {num2} é: {contador}")'''

#Questão 4
'''Escreva um programa para calcular o fatorial de um número fornecido pelo usuário.

numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("Digite um número positivo.")
else:
    fatorial = 1
    i = 1
    while i <= numero:
        fatorial *= i
        i += 1
print(f"O fatorial de {numero} é {fatorial}.")'''

#Questão 5
'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de
potência da linguagem ou o operador de exponenciação.

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1
res_expoente = expoente
if expoente >= 0:
    while expoente > 0:
        resultado *= base
        expoente -= 1
else:
    while expoente < 0:
        resultado /= base
        expoente += 1
print(f"{base} elevado a {res_expoente} é igual a {resultado}")'''

#Questão 6
'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele
deseja ver a tabuada.

numero = int(input("Digite um número de 1 a 10 para ver a tabuada: "))
if numero < 1 or numero > 10:
    print("Número inválido.")
else:
    i = 1
    print(f"Tabuada do {numero}:")
    while i <= 10:
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        i += 1'''

#Questão 7
'''A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes.
Faça um algoritmo para coletar e armazenar dados sobre o salário e número
de filhos de cada habitante e após as leituras, escrever:
a) Média de salário da população
b) Média do número de filhos
c) Maior salário dos habitantes
d) Percentual de pessoas com salário menor que R$ 150,00


total_habitantes = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
habitantes_salario_menor_150 = 0
num_habitantes = int(input("Digite o número de habitantes a serem registrados: "))
contador = 0
while contador < num_habitantes:
    print(f"Registro do habitante {contador + 1}:")
    salario = float(input("Digite o salário do habitante: "))
    num_filhos = int(input("Digite o número de filhos do habitante: "))
    total_habitantes += 1
    soma_salarios += salario
    soma_filhos += num_filhos
    if salario > maior_salario:
        maior_salario = salario
    if salario < 150:
        habitantes_salario_menor_150 += 1
    contador += 1
media_salario = soma_salarios / total_habitantes
media_filhos = soma_filhos / total_habitantes
percentual_salario_menor_150 = (habitantes_salario_menor_150 / total_habitantes) * 100
print("\nResultados:")
print(f"Média de salário da população: R${media_salario:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Maior salário dos habitantes: R${maior_salario:.2f}")
print(f"Percentual de pessoas com salário menor que R$ 150,00: {percentual_salario_menor_150:.2f}%")'''