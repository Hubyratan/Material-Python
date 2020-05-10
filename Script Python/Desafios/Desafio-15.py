kmp = float(input('Quantos quilometros voçê percorreu: '))
qd = int(input('Quantidade de dias com o carro: '))
rs = (qd*60)+(kmp*0.15)
print(f'Voçê deverá pagar R$ {rs:.2f}.\nR$ {qd*60:.2f} pelos dias.\nR$ {kmp*0.15:.2f} por km.')
