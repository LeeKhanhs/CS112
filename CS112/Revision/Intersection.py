def find_colored_segment_length(L1, R1, L2, R2):
    intersection_start = max(L1, L2)
    intersection_end = min(R1, R2)

    if intersection_start < intersection_end:
        colored_segment_length = intersection_end - intersection_start
        return colored_segment_length
    else:
        return 0

L1, R1, L2, R2 = map(int, input().split())

result = find_colored_segment_length(L1, R1, L2, R2)

print(result)