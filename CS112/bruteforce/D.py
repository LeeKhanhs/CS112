def serve(machine, items):
    total_time = 0
    for item in items:
        i = -1
        while machine[i] != item:
            i -= 1
        total_time -= i
        machine.append(machine.pop(len(machine) + i))
    return total_time

def main():
    n, m, k = map(int, input().split())
    machine = list(map(int, input().split()))[::-1]
    total_time = []
    for i in range(n):
        items = list(map(int, input().split()))
        total_time.append(serve(machine=machine, items=items))

    if len(total_time) > 0:
        print(*total_time)
    else:
        print(-1)

if __name__ == "__main__":
    main()