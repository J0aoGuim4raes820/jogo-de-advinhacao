from random import randint
from time import sleep
jogo = 'Vou pensar em um numero entre 0 e 5. Tente adivinhar...'
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'azulc': '\033[36m'}
print(f'{cores["azulc"]}=-{cores["limpa"]}' * 35)
print('{}{:^70}{}'.format(cores['verde'],jogo,cores['limpa']))
print(f'{cores["azulc"]}=-{cores["limpa"]}' * 35)
resposta = randint(0,5)
pergunta = str(input('Em qual numero eu pensei? ')).strip()
pergunta = int(pergunta)
print(f'{cores["azul"]}Processando...{cores["limpa"]}')
sleep(3)
if pergunta == resposta:
    print(f'{cores["verde"]}Parabéns! você acertou, eu pensei no numero {resposta}')
else:
    print(f'{cores["vermelho"]}Que pena! você errou eu pensei no numero {resposta}')
