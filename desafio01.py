h01 = int(input("Digite a hora da entrada: "))
m01 = int(input("Digite o minuto: "))
h02 = int(input("Digite a hora da entrada: "))
m02 = int(input("Digite o minuto: "))

somah = h01 + h02
somam = m01 + m02

if somam >= 60:
    somah += 1
    somam -= 60
if somah >= 12:
    somah -= 12
if somah >= 24:
    somah -= 24
if somah > 12:
    somah -= 12

print(f"{somah:02d}:{somam:02d}h")