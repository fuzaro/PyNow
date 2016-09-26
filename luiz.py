# coding: utf-8
import string
S = 'A2 A4,B2 C3,D1 F1'
N = 6
lista1 = S.split(',')
lista2=[]
for item in list(lista1):
    lista2.append(item.split())

for coo1,coo2 in lista2:
    print (coo1)
    print (coo2)

int(coo1[1])
coo1[0]

int(coo2[1])
coo2[0]

lista2
teste=1
board=list(string.ascii_lowercase[0:N]),list((range(1,N+1)))


ships=[['a1','a2','a3'],['b1','b2','b3'],['D2','D3','E2','E3']] 

ships[0].index('a2')
b = [(i,j) for i in board[0] for j in board[1]]
