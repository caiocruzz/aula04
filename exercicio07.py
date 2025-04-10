intervalo = 0
foraintervalo = 0
for x in range (5):
    numero = int(input("Digite um valor: "))
    if numero <10 or numero>20 :
        foraintervalo = foraintervalo +1
    intervalo = 5-foraintervalo
    #else:
      #  foraintervalo = foraintervalo+1
print(f"Encontrei {intervalo} numeros no intervalo e {foraintervalo} fora do intervalo")