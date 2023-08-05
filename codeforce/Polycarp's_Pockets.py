n = int(input())
lit1 = list(map(int, input().split()))
set_litst = set(lit1)
counts = []
for i in set_litst:
    counts.append(lit1.count(i))
print(max(counts))    
