# coding: utf-8
S = 'A2 A4,B2 C3,D1 F1'
lista1 = S.split(',')
lista2=[]
for item in list(lista1):
    lista2.append(item.split())

for coo1,coo2 in lista2:
    print (coo1)
    print (coo2)
lista2
teste=1
