def max_possible_maximum(n, k, arr):
    max_value = max(arr)
    max_index = arr.index(max_value)

    # Iterate through the array and increase elements if possible
    for i in range(n-1):
        if i != max_index and k > 0:
            diff = max_value - arr[i]
            if diff <= k:
                arr[i] += diff
                k -= diff
            else:
                arr[i] += k
                break

    return max(arr)

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read input for each test case
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # Find and print the result for each test case
    result = max_possible_maximum(n, k, arr)
    print(result)