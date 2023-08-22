def main():
    num = list([4, 7])
    count = 0
    
    a = int(input())
    
    while a > 0:
        x = a % 10
        a //= 10
        
        for i in num:
            if i == x:
                count += 1
                break
            
    for i in num:
        if count == i:
            print("YES")
            quit()
    
    print("NO")
    

if __name__ == "__main__":
    main()