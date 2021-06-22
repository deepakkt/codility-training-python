 # you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    work_S = []
    counter_paren = {
        '{': '}',
        '}': '{',
        '[': ']',
        ']': '[',
        '(': ')',
        ')': '(',
    }

    for c in S:
        if c in ['{', '[', '(']:
            work_S.append(c)
            continue

        try:
            last_paren = work_S.pop()
        except IndexError:
            return 0

        if last_paren != counter_paren[c]:
            return 0

    return 0 if work_S else 1
