c=0
r=0

if c>= 0 or r >=0:
    c = int(input('inter ur number of column : '))        
    r = int(input("Enter the number of rows you want in your array : "))

for i in range (1 , c+1):
    print (' ' * (i -1) , end ='')
    print('*' * r)
