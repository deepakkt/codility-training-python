# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6

    # start with the first height
    cuboid_stack = [H[0]]
    blocks = 1
    cuboid_sum = H[0]

    # scroll through the 2nd onwards
    for (idx, n) in enumerate(H[1:]):
        # same as last height, nothing to do
        if n == cuboid_sum:
            continue

        # so we have a height lower than existing sum of blocks
        if n < cuboid_sum:
            # keep removing blocks until existing sum becomes lower
            while n < cuboid_sum:
                cuboid_sum -= cuboid_stack.pop()
            # remember, existing some could be equal, so we don't act in that case
            if n > cuboid_sum:
                cuboid_stack.append(n - cuboid_sum)
                blocks += 1
            cuboid_sum = n
            continue

        # if a new height higher than existing sum is present
        # add the differential alone
        if n > cuboid_sum:
            cuboid_stack.append(n - cuboid_sum)
            cuboid_sum = n
            blocks += 1
            continue

    return blocks


inp = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(inp))
