def largestRectangleArea(heights):
    stack = []
    max_area = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)

    while stack:
        top = stack.pop()
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, heights[top] * width)

    return max_area

def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] = heights[j] + 1
            else:
                heights[j] = 0

        max_area = max(max_area, largestRectangleArea(heights))

    return max_area

a, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(b)]

matrix = [[str(cell) for cell in row] for row in matrix]

result = maximalRectangle(matrix)
print(result)