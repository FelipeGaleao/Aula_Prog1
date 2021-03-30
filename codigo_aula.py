## Lista de Exercicios

# Exercicio 1

lista_numeros = input("Insira o números").split(' ')
numero_1 = int(lista_numeros[0])
numero_2 = int(lista_numeros[1])

print(numero_1*numero_2)

# Exercicio 2
entrada_dados = input('Insira Matricula, Turma, Média').split(' ')
matricula = int(entrada_dados[0])
turma = str(entrada_dados[1])
media = float(entrada_dados[2])

print("O estudante da matricula ", matricula, " turma ", turma, " obteve media = ", media)
