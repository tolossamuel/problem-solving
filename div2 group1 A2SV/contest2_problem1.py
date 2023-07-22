# Input
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # Initialize the maximum cost of coloring
    max_cost = 0

    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)

    # Check if all elements are the same, in that case, the cost is 0
    if max_val == min_val:
        print(0)
    else:
        # Calculate the maximum cost of coloring
        max_cost = max_val - min_val

        print(max_cost)
