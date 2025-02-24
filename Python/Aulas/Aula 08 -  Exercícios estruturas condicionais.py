#Questão 1
'''O IMC (índice de massa corpórea) indica o grau de obesidade de uma pessoa. Este
índice é obtido pelo peso (em kg) dividido pelo quadrado da altura (em metros). 
Faça um programa que solicita o peso e altura de uma pessoa, calcule o IMC, apresente o seu valor e a avaliação.

peso = float(input('Informe quantos KG você pesa: '))
altura = float(input('Informe a sua altura: '))
imc = peso/(altura**2)
if imc <20:
    print('Você está Abaixo do normal')
elif imc >= 20 and imc <= 24:
    print('Você está Normal')
elif imc >= 25 and imc <= 29:
    print('Você está com Sobrepeso')
elif imc >= 30 and imc <= 34:
    print('Você está com Obesdidade leve')
elif imc >= 35 and imc <= 39:
    print('Você está com Obesidade moderada')
elif imc >= 40:
    print('Você está com Obesidade mórbida')'''

#Questão 2
'''Solicite um número ao usuário. Se for divisível por 3, informe “é divisível por 3”. Se
for divisível por 4, informe “é divisível por 4”. Se for divisível por 3 e 4, informe “É
divisível tanto por 3 quanto por 4”.

num = int(input('Digite um número: '))
if num % 3 == 0  and num % 4 == 0:
    divisivel = "É divisível tanto por 3 tanto por 4"
elif num % 3 == 0:
    divisivel = "É divisível por 3"
elif num % 4 == 0:
    divisivel = "É divisível por 4"
else:
    divisivel = "Não é divisível nem por 3 nem por 4"'''

#Questão 3
'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme
alíquotas abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme
o exemplo ao lado. No exemplo o valor da hora é 5 e
a quantidade de hora é 220.

valor_hora = float(input("Digite o valor da hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas
if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
else:
    desconto_ir = salario_bruto * 0.20
desconto_sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
salario_liquido = salario_bruto - desconto_ir - desconto_sindicato
print("\nFolha de Pagamento")
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}): R${salario_bruto:.2f}")
print(f"(-) IR ({desconto_ir:.2f})")
print(f"(-) Sindicato ({desconto_sindicato:.2f})")
print(f"FGTS ({fgts:.2f})")
print(f"Total de descontos ({desconto_ir + desconto_sindicato:.2f})")
print(f"Salário Líquido ({salario_liquido:.2f})")'''

#Questão 4
"""Elabore um algoritmo que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de
pagamento. Utilize os códigos a seguir para ler qual acondição de
pagamento escolhida e efetuar o cálculo adequado:

Código   Condição de pagamento
1        À vista em dinheiro ou cheque, recebe 10% de desconto
2        À vista no cartão de crédito, recebe 15% de desconto
3        Em duas vezes, preço normal de etiqueta sem juros
4        Em três vezes, preço normal de etiqueta mais juros de 10%
5        Em seis vezes, preço normal de etiqueta mais juros de 20%

preco = float(input("Digite o preço normal do produto: "))

print('''Temos 5 condições de pagamento, qual você prefere?
1 - À vista em dinheiro ou cheque, recebe 10% de desconto
2 - À vista no cartão de crédito, recebe 15% de desconto
3 - Em duas vezes, preço normal de etiqueta sem juros
4 - Em três vezes, preço normal de etiqueta mais juros de 10%
5 - Em seis vezes, preço normal de etiqueta mais juros de 20%''')

pagamento = int(input("Escolha a condição de pagamento (1 a 5): "))

if pagamento == 1:
    valor_pago = preco * 0.9  
elif pagamento == 2:
    valor_pago = preco * 0.85  
elif pagamento == 3:
    valor_pago = preco  
elif pagamento == 4:
    valor_pago = preco * 1.1  
elif pagamento == 5:
    valor_pago = preco * 1.2  

print(f"O valor a ser pago é R${valor_pago:.2f}")"""

#Questão 5
'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados
formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for
maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

num1 = float(input("Digite o primeiro lado do triângulo: "))
num2 = float(input("Digite o segundo lado do triângulo: "))
num3 = float(input("Digite o terceiro lado do triângulo: "))
if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
    if num1 == num2 == num3:
        tipo_triangulo = "Equilátero"
    elif num1 == num2 or num1 == num3 or num2 == num3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
print(f"Os lados formam um triângulo {tipo_triangulo}.")'''

#Questão 6
'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo. 
Observe os termos no plural, a colocação do "e", da vírgula,etc. 
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21,
11, 1, 7 e 16

numero = int(input("Digite um número inteiro menor que 1000: "))
if numero < 0 or numero >= 1000:
    print("Número fora do intervalo permitido.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10
palavra_centenas = "centena" if centenas == 1 else "centenas"
palavra_dezenas = "dezena" if dezenas == 1 else "dezenas"
palavra_unidades = "unidade" if unidades == 1 else "unidades"
if centenas > 0:
    if dezenas > 0 and unidades > 0:
        print(f"{numero} = {centenas} {palavra_centenas}, {dezenas} {palavra_dezenas} e {unidades} {palavra_unidades}")
    elif dezenas > 0:
         print(f"{numero} = {centenas} {palavra_centenas} e {dezenas} {palavra_dezenas}")
    elif unidades > 0:
         print(f"{numero} = {centenas} {palavra_centenas} e {unidades} {palavra_unidades}")
    else:
        print(f"{numero} = {centenas} {palavra_centenas}")
elif dezenas > 0:
    if unidades > 0:
        print(f"{numero} = {dezenas} {palavra_dezenas} e {unidades} {palavra_unidades}")
    else:
            print(f"{numero} = {dezenas} {palavra_dezenas}")
elif unidades > 0:
    print(f"{numero} = {unidades} {palavra_unidades}")
else:
    print(f"{numero} = 0")'''