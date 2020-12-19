"""Questão 2 Teste Navi"""
import math

def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat * i
        i = i + 1
    return  fat
vet=[]
for i in range(0,10):
    if i % 2 == 0:
        vet.append(3**i+7*(fatorial(i)))
    else:
        vet.append(2 ** i + 4 * (math.log(i)))

maxi = max(vet)
print(f'O maior item do vetor x está na posição: {vet.index(maxi)} e possui valor: {maxi}')

print(f'A média dos elementos contidos no vetor x é: {round(sum(vet)/len(vet),2)}')

