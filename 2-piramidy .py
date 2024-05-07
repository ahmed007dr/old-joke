#drow piramidy

x = 0
if x <= 0:
    x = int(input('enter the number of line u need : ' ))

for n in range(1,x+1):
    print (' ' * (x-n) , end= ' ' )
    print ('*' * n)