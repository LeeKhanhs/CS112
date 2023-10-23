# class work:
#     def __init__(self, id, t, d):
#         self.id = id
#         self.t = t
#         self.d = d
        
        
n = int(input())
times = []
deadline = []
for i in range(n):
    t, d = map(int, input().split())
    times.append(t)
    deadline.append(d)

times_sort = sorted(times)
result = 0
for i in range(n):
    result += (n - i) * times_sort[i]

result = sum(deadline) - result
print(result)
