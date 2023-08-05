string = input()
sh = 'hello'
c = 0
for i in range(len(string)):
    if c<5:
        if string[i]==sh[c]:
            c+=1

if c==5:
    print("YES")
else:
    print("NO")