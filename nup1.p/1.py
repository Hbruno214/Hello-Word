# Solicitar os três valores numéricos ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Encontrar o maior valor entre eles
maior_valor = max(valor1, valor2, valor3)

# Exibir o maior valor arredondado para duas casas decimais
print("O maior valor é:", round(maior_valor, 2))