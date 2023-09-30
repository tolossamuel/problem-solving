def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        size = len(s)
        odd = []
        even = []
        oddCnt = 0
        evenCnt = 0
        
        for i in range(size):
            if i % 2 == 0:
                odd.append(s[i])
            else:
                even.append(s[i])
        
        if k % 2 == 0:
            s = "".join(sorted(s))
            print(s)
        else:
            odd.sort()
            even.sort()
            result = []
            oddCnt = 0
            evenCnt = 0
            
            for i in range(n):
                if i % 2 == 0:
                    result.append(odd[oddCnt])
                    oddCnt += 1
                else:
                    result.append(even[evenCnt])
                    evenCnt += 1
            
            print("".join(result))

if __name__ == "__main__":
    main()
