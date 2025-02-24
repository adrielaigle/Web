#Questão 1
'''Escreva um programa que imprime todos os numeros de 0 até 50, incluindo-os

for i in range(0,51,1):
    print(i)'''

#Questão 2
'''Escreva um programa que imprime todos os numeros de 0 até 50, incluindo- os. 2. Modifique o programa anterior de forma que este imprima apenas os
números que são pares.

for i in range(2,51,2):
    print(i)'''

#Questão 3
'''Escreva um programa para contar a quantidade de números pares entre dois
números quaisquer fornecidos pelo usuário

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
menor_numero = min(numero1, numero2)
maior_numero = max(numero1, numero2)
contador_pares = 0
for numero in range(menor_numero, maior_numero + 1):
    if numero % 2 == 0:  
        contador_pares += 1
print(f"A quantidade de números pares entre {menor_numero} e {maior_numero} é: {contador_pares}")'''

#Questão 4
'''Escreva um programa para calcular o fatorial de um número fornecido pelo
usuário.

num = int(input('Digte um número: '))
resultado = 1 
for num in range(1,num+1):
    resultado *= num
print(f'O fatorial de {num} é: {resultado}')'''

#Questão 5
'''Faça um programa que peça dois números, base e expoente, calcule e
mostre o primeiro número elevado ao segundo número. Não utilize a função
de potência da linguagem ou o operador de exponenciação.

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1
for _ in range(expoente):
    resultado *= base
print(f"{base} elevado a {expoente} é igual a {resultado}")'''

#Questão 6
'''Você pode criar um programa em Python para gerar a tabuada de qualquer número inteiro entre 1 e 10, 
solicitando ao usuário o número para o qual ele deseja ver a tabuada. Aqui está um exemplo de código:

numero = int(input("Digite um número inteiro entre 1 e 10: "))
if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        produto = numero * i
        print(f"{numero} x {i} = {produto}")
else:
    print("Número fora do intervalo permitido.")'''

#Questão 7
'''Escreva um programa que leia um número inteiro e calcule a soma de todos
os divisores desse número, com exceção dele próprio. Ex: a soma dos
divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

numero = int(input("Digite um número inteiro: "))
soma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:  
        soma_divisores += i
print(f"A soma dos divisores de {numero}, com exceção dele próprio, é igual a {soma_divisores}")'''

#Questão 8
'''Em Matemática, o número harmônico designado por define-se como
sendo a soma da série harmónica:
Faça um programa que leia um valor n inteiro e positivo e apresente o valor
de

n = int(input("Digite um valor inteiro e positivo n: "))
soma_harmonica = 0
for i in range(1, n + 1):
    soma_harmonica += 1 / i
print(f"O valor do número harmônico Hn para n = {n} é igual a {soma_harmonica:.4f}")'''

#Questão 9
'''A série de Fibonacci é formada pela seqüência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
faça um programa capaz de gerar a série até o n-ésimo termo.

n = int(input("Digite o valor de n (número de termos desejados): "))
termo1 = 1
termo2 = 1
if n <= 0:
    print("O valor de n deve ser maior que 0.")
elif n == 1:
    print("Série de Fibonacci:")
    print(termo1)
else:
    print("Série de Fibonacci:")
    print(termo1)
    print(termo2)
    for i in range(2, n):
        termo_atual = termo1 + termo2
        print(termo_atual)
        termo1 = termo2
        termo2 = termo_atual'''

#Questão 10
'''A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
faça um programa que gere a série até que o valor seja maior que 500.

termo1 = 1
termo2 = 1
print("Série de Fibonacci:")
print(termo1)
print(termo2)
while True:
    termo_atual = termo1 + termo2
    if termo_atual > 500:
        break
    print(termo_atual)
    termo1, termo2 = termo2, termo_atual'''

#Questão 11
'''Faça um programa que calcule o fatorial de um número inteiro fornecido
pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo

n = int(input("Digite um número inteiro: "))
fatorial = 1
if n < 0:
    print("O fatorial não está definido para números negativos.")
elif n == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, n + 1):
        fatorial *= i
    print(f"{n}! = {fatorial}")'''