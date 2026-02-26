"""
Formatação básica de strings
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >20}')
print(f'{variavel: ^20}')
print(f'{variavel: <20}')
print(f'{10000.81818:0=+10,.1f}')