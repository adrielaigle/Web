#Atividade 4ª Unidade Recursividade
'''3)Crie uma função recursiva que imprima o enésimo termo da sequência de Fibonacci (1,
1, 2, 3, 5, 8, 13, 21, 34, 55, 89,…)'''

def fibonacci(n):
    if n <= 0:
        return "O valor de n deve ser maior que zero."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('DIgite um número: '))
resultado = fibonacci(n)
print(f'O {n}° termo da sequência de Fibonacci é: {resultado}')