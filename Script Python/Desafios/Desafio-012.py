v = float(input('Valor do produto? R$'))
d = float(input('Porcentagem de desconto: '))
ds = (d*v)/100
p = v-ds
print(f'Você recebeu R${ds} de desconto, e pagará somente R${p} reais')