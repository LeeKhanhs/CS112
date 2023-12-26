def cross_product_orientation(a, b, c):
    f = (b[0] - a[0]) * (b[1] + a[1]) + (c[0] - b[0]) * (c[1] + b[1]) + (a[0] - c[0]) * (a[1] + c[1])
    if f > 0:
        return 1
    if f < 0:
        return -1
    return 0

def is_point_on_line(a, b, c):
    return min(b[0], c[0]) <= a[0] <= max(b[0], c[0]) and min(b[1], c[1]) <= a[1] <= max(b[1], c[1])

def get_point_location(p, point):
    n = len(p) - 1  # Ignore the last point which is a duplicate of the first point
    is_boundary = False
    intersection_count = 0

    for i in range(n):
        orientation_result = cross_product_orientation(point, p[i], p[i + 1])
        if orientation_result == 0 and is_point_on_line(point, p[i], p[i + 1]):
            is_boundary = True
            break
        if p[i][0] <= point[0] < p[i + 1][0] and cross_product_orientation(p[i], p[i + 1], point) > 0:
            intersection_count += 1
        elif p[i + 1][0] <= point[0] < p[i][0] and cross_product_orientation(p[i + 1], p[i], point) > 0:
            intersection_count += 1

    if is_boundary:
        return "BOUNDARY"
    elif intersection_count % 2 == 1:
        return "INSIDE"
    else:
        return "OUTSIDE"

def main():
    n, m = map(int, input().split())
    polygon = []
    
    for _ in range(n):
        point = tuple(map(int, input().split()))
        polygon.append(point)
    polygon.append(polygon[0])

    for _ in range(m):
        x, y = map(int, input().split())
        result = get_point_location(polygon, (x, y))
        print(result)

if __name__ == "__main__":
    main()