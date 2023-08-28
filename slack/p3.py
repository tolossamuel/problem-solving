n = list(map(int, (input().split())))
def operation(x):
    if x > 2*n[1]:
           print("NO")
           quit()
    if x > n[1]:
        return x
    elif x < n[1]:
                if (x < 3*x):
                        operation(x*2)
                operation((x*10)+1)
    else:
           print("YES")
           quit()
y = 0
check =False
operation(n[0])

       

                
