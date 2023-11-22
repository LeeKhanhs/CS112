with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

T = lines[0]

count = 0
i = 1
while i < len(lines):
    m, n = lines[i].strip().split()
    n = int(n)
    with open(f"input_{count}.txt", "w+") as ouptut_file:
        line_write = "".join(lines[i: i + n + 1])
        ouptut_file.write(line_write)
    i = i + n + 1
    count += 1
print(count)
        