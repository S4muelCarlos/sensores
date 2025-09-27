sim = 's'
nao = 'n'

s1 = input('o sensor 1 está ligado? s/n: ')
s2  = input('o sensor2 está ligado? s/n: ')

if s1 in nao and s2 in nao:
    print(input('Desligado'))
    
else:

    print(input('Ligado'))