def orientation(p, q, r):
    # Function to determine the orientation of three points (p, q, r).
    # Returns True if the orientation is counter-clockwise or collinear.
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    return val >= 0

def convex_hull(points):
    # Sort the points based on x-coordinates
    points.sort()

    # Initialize lower and upper hulls
    lower_hull = []
    upper_hull = []

    # Build the lower hull
    for p in points:
        while len(lower_hull) >= 2 and not orientation(lower_hull[-2], lower_hull[-1], p):
            lower_hull.pop()
        lower_hull.append(p)

    # Build the upper hull
    for p in reversed(points):
        while len(upper_hull) >= 2 and not orientation(upper_hull[-2], upper_hull[-1], p):
            upper_hull.pop()
        upper_hull.append(p)

    # Combine the lower and upper hulls (excluding duplicated point)
    return lower_hull[:-1] + upper_hull[:-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = [tuple(map(int, input().split())) for _ in range(n)]
    cylinders = [tuple(map(int, input().split())) for _ in range(m)]

    # Find the convex hull of cylinders using the orientation function
    fence = convex_hull(cylinders)

    # Sort the convex hull points based on x-coordinates and then y-coordinates
    fence.sort()

    # Output: Selected wooden cylinders forming the protective fence
    for point in fence:
        print(*point)