soma = 0
cont = 0
for i in range (1, 11):
    num = int(input('Digite o {}º valor: '.format(i)))
    if num %2 != 0:
        soma += num
        cont += 1
print('Você informou', cont,' números ÍMPARES e a soma foi', soma)