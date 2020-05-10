====================================================
#  Operadores Aritméticos

# (+) Adição         |  (**) Potência
# (-) Subtração      |  (//) Divisão Inteira
# (*) Multiplicação  |  (%) Resto da Divisão
# (/) Divisão        |
====================================================
# Exemplo:

#     5+2 == 7       |   5**2 == 25
#     5-2 == 3       |   5//2 == 2
#     5=2 == 10      |   5%2  == 1
#     5/2 == 2.5     |
====================================================
#  Ordem de Precedência

# 1-[()]
# 2-[**]
# 3-[*]-[ /]-[//]-[%]
# 4-[+]-[-]
====================================================
# Hacks

# pow == Potência == **
# Raiz quadrada == X**(1/2)
# Raiz cubica == X**(1/3)
# Numero com 3 casas decimais == {:.3f}= 3flutuantes
# end=' ' == Não quebrar linha
# \n == Quebrar linha
====================================================
#       Multiplicando Palavras/Simbolos

# >>>'Olá'*5
 'oláoláoláoláolá'
# >>>'='*20
 '===================='
# >>> print('='*20)
#  ====================

# Exemplo:

Nome = str(input('Qual é seu nome ? '))
print('Prazer em te conhecer {:20} !'.format(Nome))
print('Prazer em te conhecer {:>20} !'.format(Nome))
print('Prazer em te conhecer {:<20} !'.format(Nome))
print('Prazer em te conhecer {:^20} !'.format(Nome))
print('Prazer em te conhecer {:=^20} !'.format(Nome))
print('Prazer em te conhecer {:^20} !'.format(Nome))

