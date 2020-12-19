"""Questão 3 Teste Navi"""

Aluno1 = float(input('Insira a nota do Aluno 1: '))
Aluno2 = float(input('Insira a nota do Aluno 2: '))
Aluno3 = float(input('Insira a nota do Aluno 3: '))
Aluno4 = float(input('Insira a nota do Aluno 4: '))
Aluno5 = float(input('Insira a nota do Aluno 5: '))

dict = {'Al1':Aluno1, 'Al2':Aluno2, 'Al3':Aluno3,'Al4':Aluno4, 'Al5':Aluno5}

a = dict[max(dict, key=dict.get)]

print(f'O aluno com a maior nota foi o aluno: {a} e sua nota foi: {max(dict.values())}')

