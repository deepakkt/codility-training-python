# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    num_set = set()

    for n in A:
        if n in num_set:
            num_set.remove(n)
            continue

        num_set.add(n)

    return num_set.pop()

