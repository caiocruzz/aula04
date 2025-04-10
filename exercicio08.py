soma = 0
qntdusu = int(input("Quantos numeros voce tem?: "))
for x in range (qntdusu):
    notas = float(input("Digite uma nota: "))
    soma = soma + notas
calculomedia = soma / qntdusu
print(f"A media é: {calculomedia}")