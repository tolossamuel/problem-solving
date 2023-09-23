n, query = map(int, input().split())
nums = list(map(int, input().split()))
q = list(map(int, input().split()))

color_positions = {}
result = []

# Initialize the color_positions dictionary
for i in range(n):
    if nums[i] not in color_positions:
        color_positions[nums[i]] = i + 1

# Process the queries without nested loops
for item in q:
    position = color_positions[item]
    result.append(position)

    # Move the card to the top without nested loops
    if position != 1:
        prev_position = position - 1
        prev_color = nums[prev_position - 1]
        color_positions[prev_color], color_positions[item] = position, 1

# Print the answers
print(" ".join(map(str, result)))
