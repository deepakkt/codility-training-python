# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    if B < K:
        return 0 if A > 0 else 1

    end_seed = B // K
    diff_seed = (A - 1) // K

    return end_seed - diff_seed