def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    return 0 if val == 0 else (1 if val > 0 else 2)
def is_on_line(p, q, r):
    return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])
def do_line_segments_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and is_on_line(p1, p2, q1):
        return True
    if o2 == 0 and is_on_line(p1, q2, q1):
        return True
    if o3 == 0 and is_on_line(p2, p1, q2):
        return True
    if o4 == 0 and is_on_line(p2, q1, q2):
        return True
    return False

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        coordinates = list(map(int, input().split()))
        p1 = (coordinates[0], coordinates[1])
        q1 = (coordinates[2], coordinates[3])
        p2 = (coordinates[4], coordinates[5])
        q2 = (coordinates[6], coordinates[7])
        if do_line_segments_intersect(p1, q1, p2, q2):
            print("YES")
        else:
            print("NO")