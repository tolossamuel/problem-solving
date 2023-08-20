number = int(input())
adjacency_list = [list(map(int, input().split())) for _ in range(number)]
counter_list = [0]
for y in range(number):
    for x in range(len(adjacency_list[y])):
        if adjacency_list[y][x] == 1:
            counter_list[0]+= 1
            counter_list.append(x+1)
    print(*counter_list)
    counter_list = [0]