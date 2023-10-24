def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        v = list(map(int, input().split()))
        total_sum = sum(v)
        temp = 0
        min_count = n
        count = 0

        for i in range(n):
            temp += v[i]
            count += 1
            temp_maxo = 0

            if total_sum % temp == 0:
                temp_maxo = count
                temp_sum = 0
                temp_count = 0

                for j in range(i + 1, n):
                    temp_sum += v[j]
                    temp_count += 1

                    if temp_sum == temp:
                        temp_maxo = max(temp_maxo, temp_count)
                        temp_sum = 0
                        temp_count = 0

                if temp_sum == 0:
                    min_count = min(min_count, temp_maxo)

        print(min_count)

if __name__ == "__main__":
    main()
