# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    # reformat the input to incorporate the size of the fish as well
    b_repr = [
        {'size': A[idx], 'dir': n} for (idx, n) in enumerate(B)
    ]

    fish_stack = []

    while True:
        for fish in b_repr:
            if not fish_stack:
                fish_stack.append(fish)
                continue

            if fish['dir'] == 1:
                fish_stack.append(fish)
                continue

            if fish['dir'] == 0:
                if fish_stack[-1]['dir'] == 0:
                    fish_stack.append(fish)
                    continue

                if fish_stack[-1]['size'] > fish['size']:
                    continue

                try:
                    # keep removing all downstream fish as long as the current
                    # upstream fish is larger than them
                    while fish_stack[-1]['dir'] == 1 and fish_stack[-1]['size'] < fish['size']:
                        fish_stack.pop()
                except IndexError:
                    pass

                fish_stack.append(fish)

        # decide if you want to make another pass
        # if the fish flow is unchanged then exit
        if fish_stack == b_repr:
            break

        # make another pass
        b_repr = fish_stack[:]
        fish_stack = []

    return len(fish_stack)
