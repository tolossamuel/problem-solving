number = int(input())
list_matrix = [list(map(int, input().split())) for _ in range(number)]
row = []
column = []
for i in range(number):
    counter = 0
    for y in range(number):
        if (list_matrix[i][y] == 1):
            counter+= 1
        
    if counter == 0:
        row.append(i+1)
for i in range(number):
    counter = 0
    for y in range(number):
        if (list_matrix[y][i] == 1):
            counter+= 1
        index = y+1
    if counter == 0:
        column.append(i+1)
print(len(column), *column)
print(len(row), *row)
