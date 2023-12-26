def closest_pair(points):
    points.sort(key=lambda point: point[0])  # Sort points by x-coordinate
    return closest_pair_util(points)

def closest_pair_util(points):
    n = len(points)

    if n <= 3:
        return brute_force(points)

    mid = n // 2
    mid_point = points[mid]

    left_half = points[:mid]
    right_half = points[mid:]

    left_closest = closest_pair_util(left_half)
    right_closest = closest_pair_util(right_half)

    delta = min(left_closest, right_closest)

    strip = [point for point in points if abs(point[0] - mid_point[0]) < delta]
    strip.sort(key=lambda point: point[1])

    return min(delta, strip_closest(strip, delta))

def brute_force(points):
    min_dist = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist_ij = distance(points[i], points[j])
            min_dist = min(min_dist, dist_ij)
    return min_dist

def strip_closest(strip, delta):
    n = len(strip)
    min_dist = delta

    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):
            dist_ij = distance(strip[i], strip[j])
            min_dist = min(min_dist, dist_ij)

    return min_dist

def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

if __name__ == "__main__":
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    result = closest_pair(points)
    print(result)