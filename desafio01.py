hora1=int(input("digite uma das horas"))
min1=int(input("digite uma minutagem"))
hora2=int(input("digite uma das horas"))
min2=int(input("digite uma minutagem"))

somaH=hora1+hora2
somaM=min1+min2





if somaM>=60:
    minuto=somaM-60
if somaH>=12:
    hora=somaH-60



print(f"{hora+1}:{minuto}")