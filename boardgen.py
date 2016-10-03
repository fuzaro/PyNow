import string

N=5
row, col =list(string.ascii_uppercase[0:N]),list((range(1,N+1)))
board = [(x+str(y)) for x in row
         for y in col]
