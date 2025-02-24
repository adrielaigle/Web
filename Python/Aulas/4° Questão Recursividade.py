#Atividade 4ª Unidade Recursividade
'''4) crie uma função recursiva que converte um número inteiro de decimal para binário'''

def decimal_para_binario(n):
    if n <= 0:
        return 'O número tem que ser maior que zero.'
    elif n == 1:
        return '1'
    else:
        return decimal_para_binario(n // 2) + str(n % 2)

numero_decimal = int(input('Digite um número: '))
binario_resultado = decimal_para_binario(numero_decimal)

if numero_decimal <=0:
    print(f'O número tem que ser maior que zero.')
else:
    print(f'A representação binária de {numero_decimal} é: {binario_resultado}')