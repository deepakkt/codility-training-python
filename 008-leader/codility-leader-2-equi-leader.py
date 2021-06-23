# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    len_A = len(A)

    if len_A == 1:
        return 1

    sorted_A = sorted(A)

    potential_leader = sorted_A[len_A // 2]
    leader_count = 0

    for i in A:
        if i == potential_leader:
            leader_count += 1

    # problem doesn't mention presence of a leader is guaranteed
    # so test and return 0 if there is no leader
    if leader_count <= (len_A // 2):
        return 0

    seq1_len = 0
    seq1_lead = 0

    seq2_len = len_A
    seq2_lead = leader_count

    equi = 0

    # iterate through two floating sequences
    # checking for leaders in both sequences
    # if yes, increment
    for (idx, n) in enumerate(A):
        seq1_len += 1
        seq2_len -= 1

        if n == potential_leader:
            seq1_lead += 1
            seq2_lead -= 1

        if (seq1_lead > (seq1_len // 2)) and (seq2_lead > (seq2_len // 2)):
            equi += 1

    return equi

inp =  [4, 3, 4, 4, 4, 2]
print(solution(inp))