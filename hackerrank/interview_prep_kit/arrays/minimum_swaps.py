# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

def minimum_swaps(arr):
    indexes = {i: arr[i - 1] for i in range(1, len(arr) + 1)}
    visits = [False for _ in arr]
    count = 0
    idx = 1

    while not all(visits):
        if indexes[idx] == idx:
            idx += 1
            visits[idx - 1] = True
        else:
            visits[idx - 1] = True
            idx = indexes[idx]
            if visits[idx - 1] is True:
                idx = visits.index(False) + 1
                continue
            count += 1
            visits[idx - 1] = True
            idx = arr[idx - 1]
        print(count)
    print(count)
    return count


if __name__ == "__main__":
    assert minimum_swaps([1, 4, 3, 2]) == 1
    assert minimum_swaps([4, 3, 1, 2]) == 3
    # assert minimum_swaps([7, 1, 3, 2, 4, 5, 6]) == 5
