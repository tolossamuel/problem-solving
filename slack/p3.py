n = list(map(int, (input().split())))
counter = []
def operation(x):
    counter.append(x)
    if x >3*n[1]:
           return
    if x > n[1]:
        return x
    elif x < n[1]:
                operation(x*2)
                counter.pop()
                operation((x*10)+1)
                counter.pop()
    else:
           print("YES")
           print(*counter)
           quit()
y = 0
check =False
operation(n[0])
print("NO")

       

                
