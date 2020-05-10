s = float(input('Salario? R$ '))
a = float(input('Porcentagem de aumento: '))
va = (a*s)/100
sa = s+va
print(f'Você recebeu R$ {va:.2f} de aumento! \nSeu salario agora e de R$ {sa:.2f}!')

