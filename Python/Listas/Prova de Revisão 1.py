#Questão 1

'''n = int(input("Digite um número inteiro positivo: "))
if n <= 0:
    print("O número deve ser positivo.")
else:
    numero = 1
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(numero, end=" ")
            numero += 1
        print() '''

#Questão 2

'''n = int(input("Digite o valor de 'n' para a série de Fibonacci: "))
termo1, termo2 = 1, 1
if n <= 0:
    print("O valor de 'n' deve ser maior que 0.")
elif n == 1:
    print("Série de Fibonacci até o 1º termo:")
    print(termo1)
else:
    print("Série de Fibonacci até o", n, "º termo:")
    print(termo1)
    print(termo2)

    for i in range(2, n):
        proximo_termo = termo1 + termo2
        print(proximo_termo)
        
        termo1, termo2 = termo2, proximo_termo'''

#Questão 3

'''lista_strings = ["abcdef", "abcde", "xyz", "hello", "world"]
string_mais_longa = ""
for s in lista_strings:
    tem_repetidas = False
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                tem_repetidas = True
                break
    if not tem_repetidas and len(s) > len(string_mais_longa):
        string_mais_longa = s
if string_mais_longa:
    print("A string mais longa sem letras repetidas é:", string_mais_longa)
else:
    print("Nenhuma string sem letras repetidas foi encontrada na lista.")'''

#Questão 4

'''salario_minimo = 1212.00
renda_total_cidade = 0
num_familias = 0
familias_inferior_1_salario_minimo = 0
familias_superior_10_salarios_minimos = 0

while True:
    
    num_individuos = int(input("Digite o número de indivíduos na família (ou 0 para encerrar): "))
    
    if num_individuos == 0:
        break
    
    renda_familiar = 0
    for i in range(num_individuos):
        renda_mensal = float(input(f"Digite a renda mensal do membro {i+1} da família: R$ "))
        renda_familiar += renda_mensal
    
    renda_total_cidade += renda_familiar
    renda_media_familia = renda_familiar / num_individuos
    
    if renda_media_familia < salario_minimo:
        familias_inferior_1_salario_minimo += 1
    
    if renda_media_familia > 10 * salario_minimo:
        familias_superior_10_salarios_minimos += 1
    
    num_familias += 1
renda_media_cidade = renda_total_cidade / num_familias
print(f"Renda média da cidade: R$ {renda_media_cidade:.2f}")
print(f"Percentual de famílias com renda média inferior a 1 salário mínimo: {(familias_inferior_1_salario_minimo / num_familias) * 100:.2f}%")
print(f"Quantidade de famílias com renda média superior a 10 salários mínimos: {familias_superior_10_salarios_minimos}")'''
