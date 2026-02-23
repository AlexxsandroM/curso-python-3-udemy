# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 18:46:24 2026

@author: alexs
"""

#%% Aula 1

# Permite escrever um comentario
print(123)

"""
Docstrings
"""

'''
Docstrings
'''

#%% Aula 2

# \r\n -> CRLF serve para fazer quebra de lina
# \n -> LF

print(12,34, sep='-', end='\r\n')
print(56,78, sep='', end='\n')

#%% Aula 3

# Aspas simples
print("Luiz \"Otavio\"") 


# Escape
print("Luiz \"Otavio\"") 

#%% Aula 4

# Int
print(11)
print(-11)
print(0)

# Float 

print(1.1, 10.11)
print(1.1, -1.11)

print(type(1.1))
#%% Aula 5
# Bool

print(10==10)
print(10==11)

#%% Aula 6 
# Tipos imutaveis e primitivos
# str, int, float, bool

print(int('1') + 1)
print('a' + 'b')
print(bool(''))
print(str('11') + 'b')

#%% Aula 7 
# Variaveis

nome_completo = 'Luiz Otávio Miranda'
soma_dois_mais_dois = 2 + 2
int_um = bool('1')
print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_dois)

nome = 'Luiz'
idade = 30 
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)

#%% Aula 8
# Exercicios

nome = 'Alexsandro'
sobrenome = 'Macedo'
idade = 24
ano_nascimento = 2026 - 24
maior_de_idade = idade >= 18
altura_metros = 1.73

print('Nome:', nome)
print('Sobrenome', sobrenome)
print('Idade', idade)
print('Ano de nascimento', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)

#%% Aula 9 
# Operação aritimética

adicao = 10+ 10
subtracao = 10 - 10
multiplicacao = 10 * 10
divisao = 10 / 10
divisao_inteiro = 10 // 10
exponenciacao = 2 ** 10
modulo = 55 % 2



print('Adição: ',  adicao)
print('Subtração: ', subtracao)
print('Divisão: ', divisao)
print('Divisão por inteiro: ', divisao_inteiro)
print('Exponenciação: ', exponenciacao)
print('Modulo: ', modulo)

#%% Aula 10
# Peculiaridades + e *

concatenacao = 'Alexsandro' + 'Macedo'
a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)

#%% Aula 11


# 1. (n + n)
# 2. **
# 3. + / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

#%% Aula 12 Exerc. calculo IMC

nome = 'Alexsandrp Macedo'
altura = 1.80
peso = 76
imc = peso / (altura ** 2)

print(nome, ' tem ',  altura, ' de altura pesa ', peso, ' quilos e seus IMC é ', imc)

#%% Aula 13 Exerc. calculo IMC com fstring

nome = 'Alexsandrp Macedo'
altura = 1.80
peso = 76
imc = peso / (altura ** 2)

print(f'{nome } tem {altura:.2f} de altura pesa {peso} quilos e seus IMC é {imc:.2f}')

#%% Aula 14 

a = 'A'
b = 'B'
c = '1.1'

linha = 'a={} a={} a={} a={} b{} c={}'
formato = linha.format(nome=a,nome1=b,nome2=c)

print(formato)

#%% Aula 15 Função Input

#nome = input('Qual seu nome? ')
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
soma = int_numero_1 + int_numero_2
#print(f'O seu nome é {nome=}')

print(f'A soma é {soma}')

#%% Aula 16 Funções condicionais
# if  / elif      / else
# se  / se nao se / se nao

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else: 
    print('Você não digitou nem entrar nem sair.')

#%% Aula 17 Funções condicionais
# if  / elif      / else
# se  / se nao se / se nao

condicao = False

if condicao:
    print('Este é o código do if')
else:
    print('')
    
if 10 == 10:
    print('Outro if')

#%% Aula 18 Operadores de comparação (relacionais)
"""
Op     Sig             Exemplo
>      maior           2>1
>=     maior ou igual  2>=2
<      menor           1<2
<=     menor ou igual  2<=2
==     igual           'a' == 'a'
!=     diferente       'a' != 'b'          1
"""

maior = 2>1
maior_ou_igual = 2>=2
menor = 1<2
menor_ouigual = 2<=2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(maior_ou_igual)

#%% Aula 19 Exerc. de comparação

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'Valor {primeiro_valor} (Primeiro Valor) é maior que valor {segundo_valor} (Segundo valor)')
elif primeiro_valor < segundo_valor:
    print(f'Valor {primeiro_valor} (Primeiro Valor) é menor que valor {segundo_valor} (Segundo valor)')
else:
    print('Provavelmente os 2 valores são iguais.')
    
#%% Aula 20 Operadores lógicos
"""
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdeiras
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
São considerados falsy
0 0.0 '' False
Tambem existe o tipo none que é usado para representar um valor
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')