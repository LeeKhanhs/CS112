def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise

def find_position_relative_to_car(t, test_cases):
    for i in range(t):
        p1, p2, p3 = test_cases[i][:2], test_cases[i][2:4], test_cases[i][4:]

        orientation_val = orientation(p1, p2, p3)

        if orientation_val == 0:
            print("TOUCH")
        elif orientation_val == 1:
            print("RIGHT")
        else:
            print("LEFT")
t = int(input())
test_cases = []
for _ in range(t):
    case = list(map(int, input().split()))
    test_cases.append(case)

find_position_relative_to_car(t, test_cases)