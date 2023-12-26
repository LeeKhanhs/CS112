def findMaximumLength(nums):
    n = len(nums)
    
    # Initialize an array to store the prefix sum
    s = [0] * (n + 1)
    
    # Initialize arrays to store the maximum length and previous indices
    f = [0] * (n + 1)
    pre = [0] * (n + 2)

    # Calculate the prefix sum
    for i in range(1, n + 1):
        s[i] = s[i - 1] + nums[i - 1]
    
    # Dynamic programming to find the maximum length
    for i in range(1, n + 1):
        pre[i] = max(pre[i], pre[i - 1])
        f[i] = f[pre[i]] + 1
        target = s[i] * 2 - s[pre[i]]
        
        # Find the appropriate index for updating the pre array
        j = pre[i] + 1
        while j <= n and s[j] < target:
            j += 1
        pre[j] = i
    
    # Return the maximum length
    return f[n]

# Input: Length of array
n = int(input())

# Input: Elements of the array
nums = list(map(int, input().strip().split()))

# Output: Maximum length of a non-decreasing array
print(findMaximumLength(nums))