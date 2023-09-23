n, q = map(int, input().split())
num=input().split()
color=input().split()
for y in color:    
    i=num.index(y)    
    print(i+1,end=" ");    
    num[:i+1]=[y]+num[:i]