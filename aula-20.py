"""
and (e) or (ou) not (nÃ£o)
and - Todas as condiÃ§Ãµes precisam ser verdeiras
Se qualquer valor for considerado falso, a expressÃ£o inteira serÃ¡ avaliada naquele valor
SÃ£o considerados falsy
0 0.0 '' False
Tambem existe o tipo none que Ã© usado para representar um valor
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
