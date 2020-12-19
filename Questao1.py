"""Questão 1 Teste Navi"""

start = 1
stop = 5000000 + 1
count = 0

for numero in range(start,stop):
    if numero % 2 == 0 and numero % 49 == 0 and numero % 37 == 0:
        count = count + 1

print(count)

print(f'Existem {count} números pares, múltiplos de 49 e múltiplos de 37 no intervalo de 1 a 5 milhões')