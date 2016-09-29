# coding: utf-8
import string
S = 'A2 B3,B2 C3,D1 F1,E1 E5,B1 K1,D4 D10'
N = 6
T = ['B3', 'C1', 'F1']
alfa = string.ascii_uppercase
lista1 = S.split(',')
lista2=[]
for item in list(lista1):
    lista2.append(item.split())
print(lista2)
ship = 0
ships = []
for coo1,coo2 in lista2:
    print("ship",ship," coo-> ",coo1,coo2)
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

print("ships", ships)
clone_ship = list(ships)
for x in T:
    for i in range(len(ships)):
        print(len(ships), i)
        for j in range(len(ships[i])):
            print(len(ships[i]),x,i, j)
#            if ships[i][j] == x:
#                print("fogo ", ships[i][j], " tiro ",x)
#            else:
#                print("Agua ", ships[i][j], " tiro ",x)
print(x)


                

print("clone", clone_ship)
#ships.index('A2')


#    shiptype = 2
#    if coo1[1] == coo2[1]:
#    shiptype = 1
#    if coo1[0] != coo2[]:
#    shiptype = 0
#    print (coo1)
#    print (coo2)
#    i = alfa.index(coo1[0])
#    j = alfa.index(coo2[0])


#int(coo1[1])
#oo1[0]

#int(coo2[1])
#coo2[0]

#lista2
#teste=1
#board=list(string.ascii_lowercase[0:N]),list((range(1,N+1)))


#ships=[['a1','a2','a3'],['b1','b2','b3'],['D2','D3','E2','E3']] 

#ships[0].index('a2')
#b = [(i,j) for i in board[0] for j in board[1]]
