number = int(input())
adjacency_list = [list(map(int, input().split())) for _ in range(number)]
counter = 0
for y in range(number):
    for x in range(len(adjacency_list[y])):
        if adjacency_list[y][x] == 1:
            counter += 1
print(counter//2)