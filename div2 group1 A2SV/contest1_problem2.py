n = int(input())
for i in range(n):
    m= int(input())
    ope = 0
    checker=0
    sum_of=0
    li = list(map(int,input().split()))
    for i in range(m):
        if li[i]>=0 and checker==0:
            sum_of+=li[i]
        elif li[i]<=0:
            li[i]*=-1
            checker+=1
            sum_of+=li[i]
        elif checker!=0:
                checker=0
                ope+=1
                sum_of+=li[i]
    if checker != 0:
        ope+=1
    print(f"{sum_of} {ope}")
            
            
    