

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    impacts = {
        "A": 1, "C": 2, "G": 3, "T": 4
    }

    history = dict()

    result = []
    for idx in range(0, len(P)):
        (start, end) = P[idx], Q[idx]

        dna_sequence = S[start:end+1]

        if (start, end) in history:
            result.append(history[(start, end)])
            continue

        if 'A' in dna_sequence:
            result.append(1)
            history[(start, end)] = 1
            continue

        if 'C' in dna_sequence:
            result.append(2)
            history[(start, end)] = 2
            continue

        if 'G' in dna_sequence:
            result.append(3)
            history[(start, end)] = 3
            continue

        if 'T' in dna_sequence:
            result.append(4)
            history[(start, end)] = 4
            continue


    return result

