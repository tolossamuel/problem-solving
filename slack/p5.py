parent = [-1,0,0,1,1,2]
s = "abacbe"
global checker
checker = []
global max_num
max_num = 0
global b
b = []
global a
a = 0
def dfs(counter):
    global checker
    checker.append(s[counter])
    global max_num
    global a
    
    
    if counter >= len(parent) :
                return 0
    if s[counter+1] in checker:
                a = 0
                return 0
    a += 1
    dfs(counter+1)
    
for i in range(4):
            if a > 0:
                    max_num += 1
            a = 0
            dfs(0)
            checker = []
            

print(max_num)