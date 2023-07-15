n = int(input())
names = {}
for _ in range(n):
    name = input()
    if name in names:
        names[name] += 1
        new_name = name + str(names[name])
        print(new_name)
    else:
        names[name] = 0
        print("OK")
