n, m, k = map(int, input().split())

def check(caro_matrix, i, j):
    if i < 1 or i > n or j < 1 or j > m:
        return False
    
    current = caro_matrix[i][j]
    if current + caro_matrix[i - 1][j] + caro_matrix[i][j - 1] + caro_matrix[i - 1][j - 1] == 4 or \
       current + caro_matrix[i - 1][j] + caro_matrix[i][j + 1] + caro_matrix[i - 1][j + 1] == 4 or \
       current + caro_matrix[i + 1][j] + caro_matrix[i + 1][j - 1] + caro_matrix[i][j - 1] == 4 or \
       current + caro_matrix[i][j + 1] + caro_matrix[i + 1][j] + caro_matrix[i + 1][j + 1] == 4:
        return True
    return False

if n < 2 or m < 2:
    print(0)
else:
    caro_matrix = [[0 for _ in range(m + 2)] for __ in range(n + 2)]
    result = 0
    for step in range(1, k + 1):
        i, j = map(int, input().split())
        caro_matrix[i][j] = 1
        if check(caro_matrix, i, j):
            result = step
            break
    print(result)