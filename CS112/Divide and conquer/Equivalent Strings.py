def are_equivalent(a, b):
    if a == b:
        return True
    n = len(a)
    if n % 2 == 1:
        return False
    mid = n // 2
    a1 = a[:mid]
    a2 = a[mid:]
    b1 = b[:mid]
    b2 = b[mid:]
    return (are_equivalent(a1, b1) and are_equivalent(a2, b2)) or \
           (are_equivalent(a1, b2) and are_equivalent(a2, b1))

if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    result = "YES" if are_equivalent(a, b) else "NO"
    print(result)