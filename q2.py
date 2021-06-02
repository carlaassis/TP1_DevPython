data = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))

data2 = int(input('\nDigite o dia atual: '))
mes2 = int(input('Digite o mês atual: '))
ano2 = int(input('Digite o ano atual: '))

idade_anos = ano2 - ano
if mes >= mes2:
    if mes == mes2:
        if data > data2:
            idade_anos - 1

    else:
        idade_anos - 1

dias_passados = (30 - data) + ((12 - mes) * 30) + ((mes2 - 1) * 30) + data2 + (idade_anos) * 365
print('Você viveu', dias_passados, 'dias.')