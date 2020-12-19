"""Questão 3 Teste Navi"""

Aluno1 = float(input('Insira a nota do Aluno 1: '))
Aluno2 = float(input('Insira a nota do Aluno 2: '))
Aluno3 = float(input('Insira a nota do Aluno 3: '))
Aluno4 = float(input('Insira a nota do Aluno 4: '))
Aluno5 = float(input('Insira a nota do Aluno 5: '))

dict = {'Aluno1':Aluno1, 'Aluno2':Aluno2, 'Aluno3':Aluno3,'Aluno4':Aluno4, 'Aluno5':Aluno5}

a = max (dict, key=dict.get)

print(f'O aluno com a maior nota foi o aluno: {a} e sua nota foi: {max(dict.values())}')

