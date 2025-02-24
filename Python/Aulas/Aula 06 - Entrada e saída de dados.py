#Questão 1
'''Crie um programa em Python que solicite ao usuário e receba o valor do lado para
calcular a área de um quadrado;

num1 = float(input('Digite o valor do lado do quadrado: '))
area = num1 **2
print('O valor da área do quadrado é:', area)'''

#Questão 2
'''Crie um programa em Python que solicite ao usuário e receba os valores da base
e altura para calcular a área de um triangulo;

base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))
area = (base*altura)/2
print('O valor da área do triangulo é:', area)'''

#Questão 3
'''Crie um programa em Python que que solicite ao usuário e receba o valor do raio
para calcular a área, perímetro e diâmetro de um círculo;
Declare π como constante.

raio = float(input('Digite o valor do raio: '))
PI = 3.14
area = PI*raio**2
perimetro = 2*PI*raio
diametro = 2*raio

print("o Valor da área do círculo é:", area)
print('o Valor do perímetro do círculo é:', perimetro)
print('o Valor do diametro é:',diametro)'''

#Questão 4
'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.

area = float(input('Forneça o tamanho em metros quadrados da área a ser pintada: '))
litro = 3
lata = 18
preço_lata = 80
litros_necessario = area / litro
quantidade_lata = int(litros_necessario / lata)
if litros_necessario % lata != 0:
    quantidade_lata =+ 1
preço_total = preço_lata * quantidade_lata
print(f"Você precisará de {quantidade_lata} latas de tinta.")
print(f"O preço total será de R${preço_total:.2f}")'''

#Questão 5
'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre: a) o produto do dobro do primeiro com metade do segundo. 
b) a soma do triplo do primeiro com o terceiro. 
c) o terceiro elevado ao cubo.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

produto = num1 *2* (num2/2)
soma = num1*3 + num3
elevado = num3**3

print('o produto do dobro do primeiro com metade do segundo é: {:.0f}'.format(produto))
print('a soma do triplo do primeiro com o terceiro é: {:.0f}'.format(soma))
print('o terceiro elevado ao cubo é: {:.2f} '.format(elevado))'''