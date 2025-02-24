#Atividade 4ª Unidade Recursividade
'''2)Implemente uma função recursiva que, dados dois números inteiros x e n, calcula o
valor de x n'''

def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n - 1)

base = int(input('DIgite o valor da base: '))
expoente = int(input('DIgite o valor do expoente: '))
resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a {resultado}")