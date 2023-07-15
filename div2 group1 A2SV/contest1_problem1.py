n=int(input())
for i in range(n):
    cont=[]
    win = []
    for y in range(3):
        enter=input()
        enter=list(enter)
        cont.append(enter)
    if cont[0][0]==cont[0][1] and cont[0][1] == cont[0][2] and cont[0][2]!='.':
        print(cont[0][0])
    elif cont[1][0]==cont[1][1] and cont[1][1] == cont[1][2] and cont[1][2]!='.':
        print(cont[1][0])
    elif cont[2][0]==cont[2][1] and cont[2][1] == cont[2][2] and cont[2][2]!='.':
        print(cont[2][0])
    elif cont[0][0]==cont[1][0] and cont[1][0] == cont[2][0] and cont[2][0]!='.':
        print(cont[1][0])
    elif cont[1][0]==cont[1][1] and cont[1][1] == cont[1][2] and cont[1][2]!='.':
        print(cont[1][0])
    elif cont[0][1]==cont[1][1] and cont[1][1] == cont[2][1] and cont[2][1]!='.':
        print(cont[1][1])
    elif cont[0][2]==cont[1][2] and cont[1][2] == cont[2][2] and cont[2][2]!='.':
        print(cont[1][2])
    elif cont[0][0]==cont[1][1] and cont[1][1] == cont[2][2] and cont[2][2]!='.':
        print(cont[1][1])
    elif cont[0][2]==cont[1][1] and cont[1][1] == cont[2][0] and cont[2][0]!='.':
        print(cont[1][1])
    else:
        print("DRAW")
        