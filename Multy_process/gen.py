import random


array_of_int = [random.randint(0, 100000) for _ in range(1000)]
with open("array.txt", "w+") as file:
    for i in array_of_int:
        file.write(str(i) + " ")
