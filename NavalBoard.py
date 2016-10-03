# coding: utf-8

# Este é um programa que simula um jogo de Batalha Naval
# O Objetivo deste programa é apresentar a quantidade de:
# 1 - Barcos atingidos e
# 2 - Barcos naufragados
# Deverá ser informado as seguinte variáveis :
# S ---> Barcos no formato "XN YN" sparados com virgula
# N ---> Tamanho(int<23) do Tabuleiro NxN
# T ---> Tiros
# Os barcos poderão ser:
# quadrados com 4 posicoes ==> PP
#                              PP
# linha em 3 posiçoes ==> PPP
#
# colunas em posicoes ==> P
#                         P
#                         P


import string,copy

def NavyGame(S,N,T):
    #Create constant ALPHA
    alfa = string.ascii_uppercase
    #Create Board
    row, col =list(string.ascii_uppercase[0:N]),list((range(1,N+1)))
    board = [(x+str(y)) for x in row
             for y in col]
    #Create Ship Definition
    lista1 = S.split(',')
    lista2=[]
    for item in list(lista1):
        lista2.append(item.split())

    #Test ship definition on board
    limites = []
    for p1,p2 in lista2:
        limites=limites+([p1,p2])
    for x in limites:
        try:
            t = board.index(x)
        except ValueError:
            msg = "Valor",x, " Fora  dos Limites !!!"
            print(msg)

    #Create Ships
    ship = 0
    ships = []
    for coo1,coo2 in lista2:
        l1 = str(coo1)[0]
        l2 = str(coo2)[0]
        c1 = int(str(coo1)[1:])
        c2 = int(str(coo2)[1:])
        if l1 == l2:
            for x in range(c1,c2+1):
                if x == int(c1):
                    ships.append([l1+str(x)])
                else:
                    ships[ship] = ships[ship]+[l1+str(x)]
        if c1 == c2:
            for y in alfa[alfa.index(l1):alfa.index(l2)+1]:
                if y == l1:
                    ships.append([y+str(c1)])
                else:
                    ships[ship] = ships[ship]+[y+str(c1)]
        if c1 != c2 and l1 != l2:
            for c in range(c1,c2+1):
                for l in alfa[alfa.index(l1):alfa.index(l2)+1]:
                    if l == l1 and c == c1:
                        ships.append([l+str(c)])
                    else:
                        ships[ship] = ships[ship]+[l+str(c)]
        ship += 1
    
    #clone ships Var
    clone_ship= []
    clone_ship = copy.deepcopy(ships)
        
    #Shot on ships    
    for x in T:
        for i in range(len(ships)):
            for j in range(len(ships[i])):
                if ships[i][j] == x:
                    clone_ship[i].pop(clone_ship[i].index(x))
    # Load results
    a = set([(i,len(ships[i])) for i in range(len(ships)) ])
    b = set([(i,len(clone_ship[i])) for i in range(len(clone_ship))])    
       
    #Barcos atingidos
    fired = len(ships)-len(a.intersection(b))-clone_ship.count([])
    #Barcos Afundados
    sunk = clone_ship.count([])
    
    return fired,sunk

## Barcos
S = 'A1 B2,B3 C4,D1 F1,E2 E5,D4 D6'
## Board
N = 10
## Tiros
T = ['B3', 'C1', 'F1','D4','D5','D6']

result = NavyGame(S, N, T)
print (result)
