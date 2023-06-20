# Solicitar os dados das três pessoas ao usuário
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

nome3 = input("Digite o nome da terceira pessoa: ")
idade3 = int(input("Digite a idade da terceira pessoa: "))

# Verificar qual pessoa é a mais velha
if idade1 > idade2 and idade1 > idade3:
    pessoa_mais_velha = nome1
elif idade2 > idade1 and idade2 > idade3:
    pessoa_mais_velha = nome2
else:
    pessoa_mais_velha = nome3

# Exibir a pessoa mais velha
print("A pessoa mais velha é:", pessoa_mais_velha)