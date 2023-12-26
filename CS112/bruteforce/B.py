n, m = map(int, input().split())
s = input()
mistakes = list(map(int, input().split()))
if n > 1: mistakes.append(len(s))
# Khá»i táº¡o máº£ng Äá» Äáº¿m sá» láº§n má»i phÃ­m 'q', 'w', 'e', 'r' ÄÆ°á»£c báº¥m
count = {'q': 0, 'w': 0, 'e': 0, 'r': 0}

current_combo = ""
combo_count = {'q': 0, 'w': 0, 'e': 0, 'r': 0}

for i in range(n):
    current_combo += s[i]
    combo_count[s[i]] += 1

for mistake in mistakes:
    for i in range(1, mistake + 1):
        if s[i - 1] in combo_count:
            count[s[i - 1]] += 1

# In ra káº¿t quáº£
print(count['q'], count['w'], count['e'], count['r'])