# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    from bisect import bisect_right

    quads = [
        (i - A[i], i + A[i]) for i in range(len(A))
    ]

    quads = sorted(quads, key=lambda k: k[0])

    start_coords = [
        q[0] for q in quads
    ]

    pairs = 0

    for idx, pair in enumerate(quads):
        # find position of end which covers the starts
        # this will give the absolute count
        position = bisect_right(start_coords, pair[-1])

        # subtract idx to get relative count
        # subtract 1 to exclude current pair
        pairs += (position - idx - 1)

        if pairs > 10000000:
            return -1

    return pairs
