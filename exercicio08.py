soma = 0
for x in range (5):
    notas = float(input("Digite uma nota: "))
    soma = soma + notas
    calculomedia = soma / 5
print(f"A media é: {calculomedia}")