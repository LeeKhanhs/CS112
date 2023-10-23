a, b, N, X = map(int, input().split())
if a * b > 0:
    print(max(N * (a + b), 0))
else:
    if a > 0:
        a, b = b, a
    print(max(b * X,( a + b )*(N - X)+b *X ))
