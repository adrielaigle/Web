#Aluno: Adriel Aigle Rosendo de Sá

#Questão 1
'''
num = int(input('Digite um número inteiro: '))
print(f'O número digitado foi: {num}')
'''

#Questão 2
''''
num1 = int(input('Digite o primeiro valor inteiro: '))
num2 = int(input('Digite o segundo valor inteiro: '))
num3 = int(input('Digite o terceiro valor inteiro: '))
soma = num1 + num2 + num3
print(f'A soma dos números digitados é: {soma}')
'''

#Questão 3
'''
num = int(input('Digite um número inteiro: '))
ant = num - 1 
suc = num + 1 
print(f'O antecessor de {num} é {ant} e seu sucessor é {suc}')
'''

#Questão 4
'''
c = float(input('Digite uma temperatura em Celsius: '))
f= c * (9.0 / 5.0) + 32
print(f'A temperatura em Fahrenheit é: {f:.2f}°F')
'''

#Questão 5
'''
km = float(input('Digite uma velocidade em km/h (quilômetros por hora): '))
ms = km / 3.6
print(f'A Velocidade em m/s é: {ms:.2f} m/s')
'''

#Questão 6
'''
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A Média aritmética é: {media:.1f}')
'''

#Questão 7
'''
real = float(input('Digite um valor em real: '))
cot = float(input('Digite o valor do dólar: '))
dol = real * cot 
print(f'O valor de R$:{real:.2f} em dólares é de: US$:{dol:.2}')
'''

#Questão 8
'''
raio = float(input('Digite o valor do Raio: '))
pi = 3.141592
area = pi * (raio ** 2)
print(f'A Área do Círculo é de: {area:.2f}')
'''

#Questão 9
''' 
total = 780000.00
primeiro = total * 0.46
segundo = total * 0.32
terceiro = total - primeiro - segundo
print('O prêmio total é de R$780.000,00 e será divida entre três ganhadores:') 
print(f'A quantia ganha pelo primeiro ganhador foi de R$:{primeiro:.2f}')
print(f'A quantia ganha pelo segundo ganhador foi de R$:{segundo:.2f}')
print(f'A quantia ganha pelo terceiro ganhador foi de R$:{terceiro:.2f}')
'''

#Questão 10
'''
num = float(input('Digite um número positivo: '))
if num > 0:
    quadrado = num ** 2
    raiz = num ** (1/2)
    print(f'O número ao quadrado é {quadrado}')
    print(f'A Raiz quadrada desse número é: {raiz:.2f}')
else:
     print('o Número não é positivo.')
'''

#Questão 11
'''
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número é par.')
else: 
    print('O número é ímpar.')
if num > 0:
    print('O número é positivo.')
elif num < 0:
    print('O número é negativo.')
else:
    print('O número é zero.')
'''

#Questão 12
'''
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
if nota1 >= 0.0 and nota1 <= 10.0 and nota2 >= 0.0 and nota2 <= 0.0:
    print(f'o Valor da média é: {media}')
elif nota1 < 0 and nota2 < 0:
    print('Nota inválida. A nota deve estar entre 0.0 e 10.0.')
else:
    print('Nota inválida. A nota deve estar entre 0.0 e 10.0.')
'''

#Questão 13
'''
altura = float(input('Informe sua altura em metros: '))
sexo = input('Informe seu sexo (H para Homem M para Mulher): ').upper()
if sexo == 'H':
    peso = (72.7 * altura) - 58
    print(f'o peso ideal para um homem de {altura} é de {peso:.2f}Kg')
elif sexo == 'M':
    peso = (62.1 * altura) - 44.7
    print(f'o peso ideal para uma mulher de {altura} é de {peso:.2f}Kg')'''


#Questão 14
'''
lab = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
avs = float(input("Digite a nota da avaliação semestral (0 a 10): "))
final = float(input("Digite a nota do exame final (0 a 10): "))
if lab < 0 or lab > 10 or avs <0 or avs >10 or final <0 or final >10:
    print('As notas devem estar entre 0 e 10.')
else:
    media = (lab * 2 + avs * 3 + final * 5) / 10 
if media < 3: 
    print(f'A média é de {media} o aluno está Reprovado.')
elif media < 5:
    print(f'A média é de {media} está em Recuperação.')
else:
    print(f'A média é de {media} o aluno está Aprovado.')
'''

#Questão 15
'''
p1 = input('Telefonou para a vítima? (sim/não): ')
p2 = input('Esteve no local do crime? (sim/não): ')
p3 = input('Mora perto da vítima? (sim/não): ')
p4 = input('Devia para a vítima? (sim/não): ')
p5 = input('Já trabalhou com a vítima? (sim/não): ')
sim = 0
if p1 == 'sim':
    sim = sim + 1
if p2 == 'sim':
    sim = sim + 1
if p3 == 'sim':
    sim = sim + 1
if p4 == 'sim':
    sim = sim + 1
if p5 == 'sim':
    sim = sim + 1
if sim == 2:
    print('Você é considerado(a) Suspeito(A)')
elif sim >= 3 and sim <= 4:
    print('Você é considerado(a) Cúmplice')
elif sim == 5:
    print('Você é considerado(a) Assassino(A)')
else:
    print('Você é considerado(a) Inocente')
'''

#Questão 16
'''
idade = int(input('informe sua idade: '))
serviço = int(input('Informe quanto tempo de serviço você tem em anos: '))
if idade >= 65:
    print('Apto para aposentadoria.')
elif serviço >= 30:
    print('Apto para aposentadoria.')
elif idade >= 60 and serviço >= 25:
    print('Apto para aposentadoria.')
else:
    print('Não apto para aposentadoria.')
'''

#Questão 17
'''
km = int(input('informe de quantos Km (quilômetros) foi o percurso: '))
litros = int(input('Informe em litros a quantidade de gasolina consumida: '))
consumo = km / litros
if consumo < 8:
    print('Venda o carro!')
elif consumo >= 8 and consumo <= 12:
    print('Econômico!')
elif consumo > 12:
    print('Super econômico!')
'''

#Questão 18
'''
for A in range(1,101):
    print(A)

A = 1
while A < 101:
    print(A)
    A = A + 1
'''

#Questão 19
'''
soma = 0
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    soma += valor
print(f"A soma dos 10 valores é: {soma}")
'''

#Questão 20
'''
media = 0 
for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    media += num / 10
print(f'A media dos 10 valores é: {media}')
'''

#Questão 21
'''
soma = 0
contagem = 0
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro positivo: "))
    if numero > 0:
        soma += numero
        contagem += 1

if contagem > 0:
    media = soma / contagem
    print(f"A média dos {contagem} números positivos é: {media:.0f}")
else:
    print("Nenhum número inteiro positivo foi inserido.")
'''

#Questão 22
'''
num = int(input("Digite um número inteiro N: "))
contagem = 0
numero_impar = 1
if num <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    print(f"Os {num} primeiros números naturais ímpares são:")
    while contagem < num:
        print(numero_impar)
        numero_impar += 2
        contagem += 1
'''

#Questão 23
'''
num = int(input("Digite um número inteiro positivo N: "))
if num < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    print("Números naturais de 0 até", num, "em ordem crescente:")
    for i in range(num + 1):
        print(i)
'''

#Questão 24
'''
num = int(input("Digite um número inteiro positivo N: "))
if num < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    print("Números naturais de", num, "até 0 em ordem decrescente:")
    for i in range(num, -1, -1):
        print(i)
'''

#Questão 25
'''
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma_pares = 0
multiplicacao_impares = 1
if num1 > num2:
    num1, num2 = num2, num1

for num in range(num1, num2 + 1):
    if num % 2 == 0:  
        soma_pares += num
    else:
        multiplicacao_impares *= num

print("Soma dos números pares:", soma_pares)
print("Multiplicação dos números ímpares:", multiplicacao_impares)
'''

#Questão 26
'''
for i in range(1, 10):
    print(f"Tabuada do {i}:")

    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

    print()
'''

#Questão 27
'''
num = int(input("Digite um número inteiro positivo N: "))
if num <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    numero = 1  
    for linha in range(1, num + 1):
        for coluna in range(1, linha + 1):
            print(numero, end=" ")
            numero += 1
        print() 
'''