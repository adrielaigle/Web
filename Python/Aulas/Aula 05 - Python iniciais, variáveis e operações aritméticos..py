#Questão 1 
'''Faça um Programa que dado o número de horas trabalhadas e o valor
da hora, calcule e mostre o total do salário no referido mês.

horas = float(input('Informe as horas trabalhadas: '))
valor_hora = float(input('Informe o valor da hora de trabalho: '))
salario = horas * valor_hora
print(f'o salário mensal é de: R${salario:.2f}')'''

#Questão 2
'''Você estudou muito pra sua prova de lógica de programação e conseguiu terminar a prova em 1 hora e 34 minutos. Faça um
programa que calcula e exibe o tempo de prova decorrido, em minutos e em segundos.

hora = 1
minutos = 34
tempo_minutos = (hora * 60) + minutos
tempo_segundos = tempo_minutos * 60 
print(f'O tempo total de prova em minutos foi de {tempo_minutos} minutos e em segundos foi de {tempo_segundos} segundos')'''

#Questão 3
'''Faça um Programa que converta metros para centímetros.

metros = float(input('Informe o valor em metros para ser convertido em centímetros: '))
cm = metros * 100
print (f'{metros:.2f} metros em centímetros vão equivaler a {cm:.2f} centímetros')'''

#Questão 4
'''Faça um Programa que armazene 4 notas bimestrais, calcule e imprima a média.

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a da quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'a Média das notas é de: {media:.1f}')'''

#Questão 5
'''Faça um Programa que calcule a área de um círculo de raio 5 cm.

import math
RAIO = 5
area = math.pi * RAIO ** 2
print(f'A área de um círculo com raio de 5cm é de: {area:.2f}')'''

#Questão 6
'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

base = float(input('Informe a base do quadrado: '))
altura = float(input('Informe a altura do quadrado: '))
area = base * altura
area2 = area * 2
print(f'A área do quadrado é: {area:} e o dobro dessa área é de: {area2}')'''

#Questão 7 
'''As idades das pessoas de um determinado grupo são 10, 12, 15 e 17 anos. Calcule e exiba a média de idade do grupo, e a variação
percentual da média das idades caso uma pessoa de 16 anos se junte ao grupo.

media1 = (10 + 12 + 15 + 17) / 4
media2 = (10 + 12 + 15 + 17 + 16) / 5
variaçao = ((media2 - media1) / media1) * 100
print(f"Média de idade do grupo inicial: {media1} anos")
print(f"Média de idade com a pessoa de 16 anos: {media2} anos")
print(f"Variação percentual da média: {variaçao:.2f}%")'''

#Questão 8
'''Faça um Programa que dada a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))
celsius = (fahrenheit - 32) / 1.8
print(f'A temperatura dada em {fahrenheit:.0f}°F convertida em Celsius é de: {celsius:.0f}°C')'''