# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    len_A = len(A)

    if len_A == 0:
        return -1

    if len_A == 1:
        return 0

    sorted_A = sorted(A)
    potential_leader = sorted_A[len_A // 2]
    leader_count = 0

    leader_idx = 0
    for idx, i in enumerate(A):
        if i == potential_leader:
            leader_idx = idx
            leader_count += 1

    if leader_count <= (len_A // 2):
        return -1

    return leader_idx
