from math import ceil

n, m = map(int, input().split())
p = list(map(int, input().split()))
x = list(map(int, input().split()))

d = max([(n - 1) * 100] + x)

p = p + [0 for _ in range(d // 100 - n + 10)] # coi như có 0 sinh viên

l2r = [0 for _ in range(d + 1)] # số sinh viên có thể mua tại tọa độ i từ trái qua phải


# Tìm số sinh viên có thể mua ở bên trái nếu đặt tại tọa độ i
k = -99999999999
for i in range(d + 1): # duyệt từ trái sang phải
    l = max((i + k + 1) // 2,0) # lấy trung vị
    l2r[i] = sum([p[o] for o in range(ceil(l / 100),int(i / 100)+1)]) # Nếu trường thuộc từ l -> i thì sẽ mua ở đó 
    
    if i in x:
        k = i


# tương tự

r2l = [0 for _ in range(d + 1)]

k = 9999999999999
for i in range(d, -1, -1):
    
    if i in x:
        k = i
    
    r = min(int((i + k) / 2), d)
    r2l[i] = sum([p[o] for o in range(int(r / 100),ceil(i / 100)-1,-1)])
    
    
    
    
    
    
kq = max([r2l[i] + l2r[i] if i % 100 != 0 else r2l[i] + l2r[i] - p[int(i/100)]  for i in range(d + 1)])

print(kq)