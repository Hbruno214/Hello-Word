cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumados = int(input("Por quantos anos você fumou? "))

# Calcular a quantidade total de cigarros fumados
cigarros_totais = cigarros_por_dia * 365 * anos_fumados

# Calcular a quantidade total de minutos perdidos
minutos_perdidos = cigarros_totais * 10

# Calcular a quantidade de dias perdidos (considerando 24 horas por dia)
dias_perdidos = minutos_perdidos / (60 * 24)

# Exibir o total de dias perdidos
print("Um fumante perderá aproximadamente", int(dias_perdidos), "dias de vida.")