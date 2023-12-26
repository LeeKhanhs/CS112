def solve():
    n = int(input())
    
    arr = list(map(int, input().split()))
    arr.sort()
    
    ans = 0
    if sum(arr) % 2 == 1:
        ans = 1
        arr[0] -= 1
    k = sum(arr) // 2
    c = i = 0
    
    while i < n and c + arr[i] <= k:
        c += arr[i]
        i += 1
    
    ans = ans + k + (n - i)
    return ans

def main():
    t = int(input())
    results = []
    for _ in range(t):
        results.append(solve())
    for result in results:
        print(result)

if __name__ == "__main__":
    main()