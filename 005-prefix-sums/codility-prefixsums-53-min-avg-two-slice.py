def solution(A):
    # write your code in Python 3.6
    alen = len(A)
    prefix_sums = [0] * alen
    current_sum = 0

    for (i, n) in enumerate(A):
        current_sum += n
        prefix_sums[i] = current_sum

    min_average = 99999
    min_slice = 999999

    # note: this relies on the mathematical concept that a slice with the lowest
    # average can always be found to be composed of other subslices of length 2
    # or 3 within the main slice
    # IMO, this is not an ideal problem statement as it relies on knowledge of a
    # mathematical concept

    for outer in range(0, alen - 1):
        for inner in range(outer + 1, outer + 4):
            if inner >= alen:
                continue

            slice_sum = prefix_sums[inner]
            if outer != 0:
                slice_sum -= prefix_sums[outer - 1]

            slice_average = slice_sum / (inner - outer + 1)
            if slice_average < min_average:
                min_average = slice_average
                min_slice = outer

    return min_slice
