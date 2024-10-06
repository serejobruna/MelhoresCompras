nome = input("Informe seu nome: ")
lugar = input("Informe o lugar: ")
print(f'Bem-vindo {nome:>20}!\nVocê chegou em {lugar:#^30}.')

numero = float(input('Escolha um numero aleatório: '))
print('Apresentando o número {param:*>+10%}'.format(param=numero))

numero = float(input('Escolha um numero aleatório: '))
print('Apresentando o número {param:*>-10.2f}'.format(param=numero))

numero = float(input('Escolha um numero aleatório: '))
print('Apresentando o número {param:*>+20e}'.format(param=numero))

numero = float(input('Escolha um numero aleatório: '))
print('Apresentando o número {param:*>-10.2f}'.format(param=numero))

saudacao = 'Bem-vindo {}! Você chegou em {}.'.format('Jedi', 'Alderaan')
print(saudacao)

saudacao = 'Bem-vindo {nome}! Você chegou em {lugar}. '            'Prossiga para o controle {inspecao}'.format(lugar='Alderaan', nome="Jedi", inspecao="area 4")
print(saudacao)

objeto = input('O que você está aprendendo agora? ')
print('Estou adorando aprender {param}'.format(param=objeto))

objeto = input('O que você está aprendendo agora? ')
print('Estou adorando aprender {param:*^20}'.format(param=objeto))

