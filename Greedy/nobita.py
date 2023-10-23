n = int(input())
ranges = []

for i in range(n):
    start, end = map(int, input().split())
    ranges.append([start,end])
    
sorted_range = sorted(ranges, key=lambda x: x[1])
# print(sorted_range)
count = 0
time = 1
# prev = None

for item in sorted_range:
    # if not prev:
    #     prev = item
    #     count += 1
    #     time = item[1]
    #     # print(item)
    #     continue
    
    if item[0] >= time:
        time = item[1]
        count += 1
        # print(item)
print(count)