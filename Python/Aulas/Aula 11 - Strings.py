#Questão 1
''' Faça um programa que leia 2 strings e informe o conteúdo delas seguido do
seu comprimento. Informe também se as duas strings possuem o mesmo
comprimento e são iguais ou diferentes no conteúdo. 

s = str(input('Digite uma palavra: '))
s2 = str(input('Digite outra palavra: '))
print(f'O comprimento de {s} é: ', len(s))
print(f'O comprimento de {s2} é: ', len(s2))
if len(s) == len(s2):
    print('Tem o mesmo comprimento')
else:
    print('Não tem o mesmo comprimento')

if s == s2:
    print('As Strigs tem o mesmo contéudo')
else:
    print('As Strigs não tem o mesmo contéudo')'''

#Questão 2
'''Faça um programa que permita ao usuário digitar o seu nome e em seguida
mostre o nome do usuário de trás para frente utilizando somente letras
maiúsculas. Dica: lembre-se que ao informar o nome, o usuário pode digitar
letras maiúsculas ou minúsculas.

nome = input("Digite seu nome: ")
nome = nome.upper()
nome_invertido = nome[::-1]
print(f"Seu nome de trás para frente em letras maiúsculas é: {nome_invertido}")'''

#Questão 3
'''Faça um programa que solicite uma string ao usuário e em
seguida a imprima em formato de escada.

texto = input("Digite uma string: ")
for i in range(len(texto)):
    print(texto[:i+1])'''

#Questão 4
'''Altere o programa anterior de modo que a escada seja
invertida.

texto = input("Digite uma string: ")
for i in range(len(texto), 0, -1):
    print(texto[:i])'''

#Questão 5
'''Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da
direita para esquerda ou vice-versa. Por exemplo: OSSO e OVO são palíndromos. Em
textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO
ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma seqüência de caracteres, mostre-a e diga se é um
palíndromo ou não. 

sequencia = input("Digite uma sequência de caracteres: ")
sequencia = ''.join(e for e in sequencia if e.isalnum()).lower()
sequencia_invertida = sequencia[::-1]
if sequencia == sequencia_invertida:
    print("A sequência é um palíndromo.")
else:
    print("A sequência não é um palíndromo.")'''

#Questão 6
'''Faça uma função que recebe uma string que representa uma cadeia de DNA e gera a
cadeia complementar. A entrada e saída de dados deve ser feita pelo programa
principal. 
Exemplo:
Entrada: AATCTGCAC
Saída: TTAGACGTG

dna_original = input("Digite uma cadeia de DNA: ")
cadeia_complementar = ""
for nucleotideo in dna_original:
    if nucleotideo == 'A':
        cadeia_complementar += 'T'
    elif nucleotideo == 'T':
        cadeia_complementar += 'A'
    elif nucleotideo == 'C':
        cadeia_complementar += 'G'
    elif nucleotideo == 'G':
        cadeia_complementar += 'C'
print("Cadeia Complementar:", cadeia_complementar)'''

#Questão 7
'''Faça um programa que leia uma data de nascimento no formato
dd/mm/aaaa e imprima a data com o mês escrito por extenso. Exemplo:
Data = 20/02/1995
Resultado gerado pelo programa:
Você nasceu em 20 de fevereiro de 1995

data_nascimento_str = input("Digite a data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data_nascimento_str.split('/')
meses = {
    '01': 'janeiro',
    '02': 'fevereiro',
    '03': 'março',
    '04': 'abril',
    '05': 'maio',
    '06': 'junho',
    '07': 'julho',
    '08': 'agosto',
    '09': 'setembro',
    '10': 'outubro',
    '11': 'novembro',
    '12': 'dezembro'
}
print(f"Você nasceu em {dia} de {meses[mes]} de {ano}")'''

#Questão 8
'''Escreva um programa que leia duas strings. Verifique se a segunda ocorre
dentro da primeira e imprima a posição de início. 
1a string: AABBEFAATT
2a string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
posicao = string1.find(string2)
if posicao != -1:
    print(f"{string2} encontrado na posição {posicao + 1} de {string1}")
else:
    print(f"{string2} não encontrado em {string1}")'''

#Questão 9
'''Escreva um programa que leia duas strings e gere uma terceira com os
caracteres comuns às duas strings lidas. 
1a string: AAACTBF
2a string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve
conter todas as letras comuns a ambas.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string_comum = ""
for char in string1:
    if char in string2 and char not in string_comum:
        string_comum += char
print(f"Resultado: {string_comum}")'''

#Questão 10
'''Conta espaços e vogais. Dado uma string com uma frase informada pelo
usuário (incluindo espaços em branco), conte: quantos espaços em branco
existem na frase. quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Digite uma frase: ")
espacos_em_branco = 0
vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
frase = frase.lower()
for char in frase:
    if char == ' ':
        espacos_em_branco += 1
    elif char in vogais:
        vogais[char] += 1
print(f"Espaços em branco na frase: {espacos_em_branco}")
for vogal, quantidade in vogais.items():
    print(f"{vogal}: {quantidade}")'''

#Questão 11
'''Escreva um programa que leia uma string e imprima quantas vezes cada
caractere aparece nessa string. 
String: TTAAC
Formato de saída:
T: 2x
A: 2x
C: 1x

string = input("Digite uma string: ")
contagem_caracteres = {}
for char in string:
    if char in contagem_caracteres:
        contagem_caracteres[char] += 1
    else:
        contagem_caracteres[char] = 1
for char, contagem in contagem_caracteres.items():
    print(f"{char}: {contagem}x")'''

#Questão 12
'''Número por extenso. Escreva um programa que solicite ao usuário a
digitação de um número até 99 e imprima-o na tela por extenso.

nomes_ate_dezenove = [
    "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove"
]
nomes_dezenas = [
    "vinte", "trinta", "quarenta", "cinquenta",
    "sessenta", "setenta", "oitenta", "noventa"
]
numero = int(input("Digite um número entre 1 e 99: "))
if 1 <= numero <= 99:
    if numero <= 19:
        extenso = nomes_ate_dezenove[numero - 1]
    else:
        dezena = numero // 10
        unidade = numero % 10
        extenso = nomes_dezenas[dezena - 2]
        if unidade > 0:
            extenso += f" e {nomes_ate_dezenove[unidade - 1]}"
    print(f"{numero} por extenso: {extenso}")
else:
    print("Número fora do intervalo permitido.")'''

#Questão 13
'''Faça um programa que leia uma palavra e some 1 no valor ASCII de cada
caractere da palavra. Imprima a string resultante.

palavra = input("Digite uma palavra: ")
palavra_resultante = ""
for char in palavra:
    novo_valor_ascii = ord(char) + 1
    novo_char = chr(novo_valor_ascii)
    palavra_resultante += novo_char
print("Palavra resultante:", palavra_resultante)'''

#Questão 14
'''Faça um programa que solicite ao usuário uma string e modifique a string
para que todos os caracteres fiquem em maiúsculas. Obs: Não utilize a função upper(). Utilize a tabela ASCII.

string = input("Digite uma string: ")
string_maiuscula = ""
for char in string:
    if 'a' <= char <= 'z':
        char_maiusculo = chr(ord(char) - 32)
        string_maiuscula += char_maiusculo
    else:
        string_maiuscula += char
print("String em maiúsculas:", string_maiuscula)'''


#Questão 15
'''Faça um programa em que troque todas as ocorrencias de uma letra L1 pela
letra L2 e da L2 pela L1 em uma string. A string e as letras L1 e L2 devem ser
fornecidas pelo usuario. Obs: Não utilize a função replace().

string = input("Digite uma string: ")
l1 = input("Digite a letra L1: ")
l2 = input("Digite a letra L2: ")
string_resultante = ""
for char in string:
    if char == l1:
        string_resultante += l2
    elif char == l2:
        string_resultante += l1
    else:
        string_resultante += char
print("String com as letras trocadas:", string_resultante)'''