def some():
    n = int(input())
    x = [int(i) for i in input().split()][:n]
    x.sort()
 
    
    y = x[0]+1
    x.pop(0)
    x.append(y)
    z=x[0]
    for i in range(1, len(x)):
        #for j in range(i):
            
        z = x[i ] * z
        
        
        
    print(z)
y = int(input())
for i in range(y):
	some()