# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    from itertools import combinations
    # write your code in Python 3.6

    # the general idea
    # 1) check the edges and handle fully positive / fully negative cases
    # 2) If mixed, do all combinations for the first three and last three (20 combinations)

    sorted_a = sorted(A)

    maxnum = sorted_a[-1]
    minnum = sorted_a[0]

    if (minnum > 0):
        return A[-1] * A[-2] * A[-3]

    if (maxnum < 0):
        return A[0] * A[1] * A[2]

    if len(sorted_a) <= 6:
        subset = sorted_a[:]
    else:
        subset = sorted_a[0:3] + sorted_a[-3:]

    maxproduct = -1000000000

    for triplet in combinations(subset, 3):
        product = triplet[0] * triplet[1] * triplet[2]

        if product > maxproduct:
            maxproduct = product

    return maxproduct
