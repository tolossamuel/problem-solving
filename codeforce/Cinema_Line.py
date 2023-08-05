n = int(input())
num = list(map(int, input().split()))
check_list = list([0, 0, 0])

for r in num:
    if r == 100:
        check_list[0] += 1
        if check_list[1] > 0:
            check_list[1] -= 1
            check_list[2] -= 1
        else:
            check_list[2] -= 3
    elif r == 50:
        check_list[1] += 1
        check_list[2] -= 1
    else:
        check_list[2] += 1
    
    if check_list[1] < 0 or check_list[2] < 0:
        print("NO")
        quit()

print("YES")