#Questão 1
'''Ler três números inteiros e mostrar o maior e o menor deles.

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digte o terceiro número:"))
 if (num1 > num2) and (num1>num3):
    print(num1, "É o maior número")
elif(num2 > num1) and (num2 > num3):
    print(num2, "É o maior número")
elif(num3 > num1) and (num3 > num2):
    print(num3, "É o maior número")
if(num1 < num2) and (num1 <num3):
    print(num1, "É o menor número")
elif(num2 < num1) and (num2 < num3):
    print(num2, "É o menor número")
elif(num3 < num1) and (num3 < num2):
    print(num3, "É o menor número")'''

#Questão 2
'''Dados três valores distintos, fazer um programa que, após a leitura destes dados, coloque-os em ordem crescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
menor = min(num1, num2, num3)
maior = max(num1, num2, num3)
meio = num1 + num2 + num3 - menor - maior
print("Os Valores em ordem crescente são:", menor, meio, maior)'''

#Questão 3
'''Elaborar um algoritmo que, dada a idade de um nadador, classificá-lo nas
categorias: infantil A (5 - 7 anos), infantil B (8 -10 anos), juvenil A (11 - 13
anos), juvenil B (14 -17 anos) e adulto (maiores que 18 anos).

idade = int(input('Digite a idade do nadador: '))
if idade >= 1 and idade <= 4:
    print('Idade fora das categorias.')
elif idade >= 5 and idade <= 7:
    print('Infatil A')
elif idade >= 8 and idade <= 10:
    print('Infatil B')
elif idade >= 11 and idade <= 13:
    print('Juvenil A')
elif idade >= 14 and idade <= 17:
    print('juvenil B')
elif idade > 18:
    print('Adulto')
else:
    print('Idade fora das categorias.')'''

#Questão 4
'''Ler um número inteiro e mostrar uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo.

num = int(input('DIgite um número inteiro: '))
if num % 2 == 0:
    par_impar = "par"
else:
    par_impar= "impar"
if num > 0:
    positivo_negativo = "positivo"
elif num < 0:
    positivo_negativo = "negativo"
else:
    positivo_negativo = "zero"
print(f"O número {num} é {par_impar} e {positivo_negativo}.")'''

#Questão 5
'''Uma empresa concederá um aumento de salário aos seus funcionários,
variável de acordo com o cargo, conforme a tabela abaixo. Faça um
programa que leia o salário e o código do cargo de um funcionário e calcule
o seu novo salário. Se o cargo do funcionário não estiver na tabela, ele
deverá, então, receber 15% de aumento. Mostre o salário antigo, o novo
salário e a diferença entre ambos.

código |  %  
310    | 5.0 
456    | 7.5 
885    | 10.0

tabela_aumento = {
    1: 0.10,  # Cargo 1: 10% de aumento
    2: 0.15,  # Cargo 2: 15% de aumento
    3: 0.20,  # Cargo 3: 20% de aumento
}
salario = float(input("Digite o salário do funcionário: "))
codigo_cargo = int(input("Digite o código do cargo do funcionário: "))
if codigo_cargo in tabela_aumento:
    aumento_percentual = tabela_aumento[codigo_cargo]
else:
    aumento_percentual = 0.15 
novo_salario = salario + (salario * aumento_percentual)
diferenca_salario = novo_salario - salario
print(f"Salário antigo: R${salario:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")
print(f"Diferença: R${diferenca_salario:.2f}")'''

#Questão 6
'''Construa a tabela-verdade para as seguintes expressões:
(p and q) and not(p or q)
not(p and not q) or q

print("p | q | (p and q) and not(p or q) | not(p and not q) or q")
for p in [True, False]:
    for q in [True, False]:
        result1 = (p and q) and not (p or q)
        result2 = not (p and not q) or q
        print(f"{p} | {q} | {result1} | {result2}")'''
