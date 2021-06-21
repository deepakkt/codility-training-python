# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    # keep only positive numbers and sort the array
    sub_A = [x for x in A if x > 0]
    sub_A = sorted(sub_A)

    for i in range(len(sub_A) - 2):
        # we found one valid triangle, just return successfully
        if sub_A[i] + sub_A[i + 1] > sub_A[i + 2]:
            return 1

    return 0
