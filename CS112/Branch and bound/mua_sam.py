def find_maximum_notes(m, n, values):
    # The result to be returned
    result = []

    def backtrack(path, remaining_value, index):
        nonlocal result  # Use nonlocal to modify the result variable in the outer scope

        # Condition to stop the recursion
        if remaining_value == 0:
            # If the result is empty or the current path is longer than the current best path
            if not result or len(path) > len(result[0]):
                result.clear()  # Remove all paths
                result.append(path[:])  # Add the new path
            # If the current path has the same length as the current best path but is lexicographically smaller
            elif len(path) == len(result[0]) and path < result[0]:
                result.clear()  # Remove all paths
                result.append(path[:])  # Add the new path
            return

        # Check if the index is out of bounds
        if index >= n:
            return

        # First branch and bound condition
        # If the length of the result is greater than the current path length plus remaining_value // values[index][0]
        # This means if we add some new value in the lowest boundary case, it can't improve the result
        if len(result) > len(path) + remaining_value // values[index][0]:
            return

        value, quantity = values[index]

        # Integrate the invalid cases where we can't take the quantity of that value
        # Second branch and bound condition
        for count in range(min(remaining_value // value, quantity) + 1):
            # Integrate all cases where we can get the quantity of values
            for _ in range(count):
                path.append(value)  # Add value to the path
            # Recursively find the next value in the path
            backtrack(path, remaining_value - value * count, index + 1)
            
            # Backtrack to explore a new branch
            for _ in range(count):
                path.pop()

    path = []
    backtrack(path, m, 0)

    if not result:  # If there is no solution
        print("0")
        return

    print(len(result[0]))  # Print the number of notes needed
    print(*result[0])  # Print the notes in the optimal path


def main():
    # Input
    n, m = map(int, input().split())
    values = []
    for _ in range(n):
        a, b = map(int, input().split())
        values.append((a, b))

    # Prioritize the low value to ensure the maximum quantity
    values.sort()

    find_maximum_notes(m, n, values)


if __name__ == "__main__":
    main()