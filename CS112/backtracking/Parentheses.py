def is_valid(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')' and stack:
            stack.pop()
        else:
            return False
    return len(stack) == 0

def backtrack(s, idx, curr, result):
    if idx == len(s):
        if is_valid(curr):
            result.append(curr)
        return
    backtrack(s, idx + 1, curr + s[idx], result)
    backtrack(s, idx + 1, curr, result)
    
def solve(S):
    result = []
    backtrack(S, 0, "", result)
    max_length = max(len(s) for s in result)
    valid_strings = [s for s in result if len(s) == max_length]
    valid_strings.sort()
    return max_length, valid_strings[0]

S = input().strip()
k, S_new = solve(S)


print(k)
print(S_new)