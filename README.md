distancia = float(input("Digite a distância da entrega em quilômetros: "))

if distancia <= 500:
    print("Recomenda-se fazer a entrega por transporte terrestre.")
else:
    print("Recomenda-se fazer a entrega por transporte aéreo.")