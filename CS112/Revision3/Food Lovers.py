def calculate_max_satisfaction(N, M, days):
    # Initialize arrays to store cumulative satisfaction levels
    left_sums = [0] * (M + 1)
    right_sums = [0] * (M + 1)
    
    # Variable to store the maximum satisfaction
    max_satisfaction = 0

    # Process each day's information
    for i in range(N):
        left, right, satisfaction = days[i]
        left_sums[right] += satisfaction  # Accumulate satisfaction from the left side
        right_sums[left] += satisfaction  # Accumulate satisfaction from the right side

    # Calculate cumulative satisfaction levels for both sides
    for i in range(1, M + 1):
        left_sums[i] += left_sums[i - 1]

    for i in range(M - 1, 0, -1):
        right_sums[i] += right_sums[i + 1]

    # Find the optimal point to leave a dish for others and update max_satisfaction
    for i in range(1, M):
        max_satisfaction = max(max_satisfaction, left_sums[i - 1] + right_sums[i + 1])

    return max_satisfaction

# Input
N, M = map(int, input().split())
days = [tuple(map(int, input().split())) for _ in range(N)]

# Output
result = calculate_max_satisfaction(N, M, days)
print(result)