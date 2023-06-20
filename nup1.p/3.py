# Solicitar os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Mostrar as opções disponíveis
print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Ler a escolha do usuário
escolha = int(input("Digite o número da operação desejada: "))

# Realizar a operação selecionada
if escolha == 1:
    resultado = numero1 + numero2
    operacao = "soma"
elif escolha == 2:
    resultado = numero1 - numero2
    operacao = "subtração"
elif escolha == 3:
    resultado = numero1 * numero2
    operacao = "multiplicação"
elif escolha == 4:
    if numero2 != 0:  # Verificar se o divisor é diferente de zero
        resultado = numero1 / numero2
        operacao = "divisão"
    else:
        print("Erro: divisão por zero não é permitida!")
else:
    print("Opção inválida!")

# Exibir o resultado da operação
if escolha in [1, 2, 3, 4]:
    print(f"O resultado da {operacao} é: {resultado}")