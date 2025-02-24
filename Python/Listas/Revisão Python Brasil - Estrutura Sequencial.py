#Questão 1 - Estrutura Sequencial

'''print('Alô mundo.')'''

#Questão 2 - Estrutura Sequencial

'''num = int(input('Digite um número: '))
print(f'O número digitado foi: [{num}]')'''

#Questão 3 - Estrutura Sequencial

'''num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
soma = num1 + num2 
print(f'A soma de {num1} com {num2} é: {soma}')'''

#Questão 4 - Estrutura Sequencial

'''soma = 0
for i in range (4):
    nota = float(input(f'Informe a {i+1}° nota: '))
    soma += nota
media = soma / 4
print(f'A média das notas é {media:.2f}')'''

#Questão 5 - Estrutura Sequencial

'''metros = int(input('Informe o valor em metros para conversão: '))
centimetros = metros * 100 
print(f'{metros} metros equivalem a {centimetros} centímetros.')'''

#Questão 6 - Estrutura Sequencial

'''raio = float(input('Forneça o raio do círculo: '))
import math 
area = math.pi * (raio ** 2)
print(f'A área do círculoc com raio {raio} é de {area:.2f}.')'''

#Questão 7 - Estrutura Sequencial

'''base = float(input('Informe a base do quadrado: '))
altura = float(input('Informe a altura do quadrado: '))
area = base * altura 
print(f'A área do quadrado com base {base} e {altura} é de: {area}')'''

#Questão 8 - Estrutura Sequencial

'''valor_hora = float(input('Quanto você ganha por hora?: '))
horas_trabalhadas = float(input('Quantas horas você trabalhou no mês?: '))
salario = valor_hora * horas_trabalhadas
print(f'O salário total desse mês é de: R${salario:.2f} ')'''

#Questão 9 - Estrutura Sequencial

'''fahrenheit = float(input('Forneça uma temperatura em Fahrenheit: '))
celsius = 5 * ((fahrenheit-32) / 9)
print(f'{fahrenheit}°F equivalem a {celsius:.1f}°C')'''

#Questão 10 - Estrutura Sequencial

'''celsius = float(input('Forneça uma temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32 
print(f'{celsius}°C equivalem a {fahrenheit:.1}°F')'''

#Questão 11 - Estrutura Sequencial

'''num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe um segundo número inteiro: '))
num3 = float(input('Informe um número real: '))
produto = num1 * 2 + (num2/2)
soma = (num3 * 3) + num3
elevado = num3 ** 3
print(f'O produto do dobro do primeiro com metado do segundo é de: {produto}')
print(f'A soma do triplo do primeiro com o terceiro é de: {soma}')
print(f'O terceiro elevado ao cubo é: {elevado:.1f}')'''

#Questão 12 - Estrutura Sequencial

'''altura = float(input('Informe sua altura em metros: '))
peso = (72.7 * altura) - 58
print(f'O peso ideal para seu corpo é de: {peso:.2f}')'''

#Questão 13 - Estrutura Sequencial

'''while True:
    sexo = str(input('Você é homem ou mulher [H/M]?: ')).upper()
    if sexo =='H':
        altura = float(input('Informe sua altura em metros: '))
        pesoH = (72.7 * altura) - 58
        print(f'O peso ideal para um Homem de {altura:.1f} metros é de {pesoH:.2f}kg')
        break
    elif sexo == 'M':
        altura = float(input('Informe sua altura em metros: '))
        pesoM = (62.1 * altura) - 44.7
        print(f'O peso ideal para uma mulher de {altura:.1f} metros é de {pesoM:.2f}kg')
        break
    else:
        print('Sexo não reconhecido. Por favor, insira H para homem ou M para mulher.')'''

#Questão 14 - Estrutura Sequencial

'''peso = float(input('Informe o peso dos peixes em quilo: '))
limite = 50
if peso > limite:
    excesso = peso - limite
    multa = excesso * 4
    print(f'João excedeu o pesso em {excesso:.2f}kg.')
    print(f'O valor a pagar da multa é de: R${multa:.2f}')
else:
    excesso = 0
    multa = 0
    print('João não excedeu o limite de peso. Portanto não há multas para pagar.')'''

#Questão 15 - Estrutura Sequencial

"""valor = float(input('Quanto você ganha por hora?: '))
horas = float(input('Quantas horas você trabalha por mês?: '))
salario_bruto = valor * horas
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - imposto_renda - inss - sindicato 
print(f'''+ Salário Bruto : R${salario_bruto:.2f}
- IR (11%) : R${imposto_renda:.2f}
- INSS (8%) : R${inss:.2f}
- Sindicato ( 5%) : R${sindicato:.2f}
= Salário Liquido : R${salario_liquido:.2f}''')"""

#Questão 16 - Estrutura Sequencial

'''metros = int(input('Informe o tamanho em metros quadrados da área a ser pintada: '))
litro = 3
lata = 18 
preço = 80
litros_necessarios = metros / litro 
quantidade_latas = int(litros_necessarios / lata)
if litros_necessarios % lata != 0:
    quantidade_latas += 1
preço_total = preço * quantidade_latas
print(f"Você precisará de {quantidade_latas} latas de tinta.")
print(f"O preço total será de R${preço_total:.2f}")'''

#Questão 17 - Estrutura Sequencial

'''import math
area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))
litros_necessarios = area / 6
litros_necessarios += litros_necessarios * 0.1
litros_necessarios = math.ceil(litros_necessarios)
latas_18_litros = litros_necessarios // 18
resto = litros_necessarios % 18
galoes_3_6_litros = math.ceil(resto / 3.6)
preco_latas = latas_18_litros * 80
preco_galoes = galoes_3_6_litros * 25
preco_misturado = (latas_18_litros * 80) + (galoes_3_6_litros * 25)
print(f"Quantidade de tinta necessária: {litros_necessarios} litros")
print(f"Situação 1 - Comprar apenas latas de 18 litros:")
print(f"  - Latas: {latas_18_litros}")
print(f"  - Preço: R$ {preco_latas:.2f}")
print(f"Situação 2 - Comprar apenas galões de 3,6 litros:")
print(f"  - Galões: {galoes_3_6_litros}")
print(f"  - Preço: R$ {preco_galoes:.2f}")
print(f"Situação 3 - Misturar latas e galões para minimizar desperdício:")
print(f"  - Latas: {latas_18_litros}")
print(f"  - Galões: {galoes_3_6_litros}")
print(f"  - Preço: R$ {preco_misturado:.2f}")'''

#Questão 18 - Estrutura Sequencial

'''tamanho = float(input('Informe o tamanho do arquivo em MB: '))
internet = float(input('Informe a velocidade de internet em Mbps: '))
tamanho_arquivo_bits = tamanho * 8 * 1024 * 1024 
tempo_download_segundos = tamanho_arquivo_bits / (internet * 1e6)  
tempo_download_minutos = tempo_download_segundos / 60
print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")'''