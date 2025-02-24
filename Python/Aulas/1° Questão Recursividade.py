#Atividade 4ª Unidade Recursividade
'''1) Defina a função recursiva div que recebe como argumentos dois números naturais m e
n e devolve o resultado da divisão inteira de m por n. Neste exercício não pode recorrer às
operações aritméticas de multiplicação, divisão e resto da divisão inteira. 2.'''

def div(m, n, count=0):
    if m < n:
        return count
    else:
        return div(m - n, n, count + 1)

m = int(input('DIgite um número natural: '))
n = int(input('DIgite um segundo número natural: '))
resultado = div(m, n)
print(f"A divisão inteira de {m} por {n} é {resultado}")