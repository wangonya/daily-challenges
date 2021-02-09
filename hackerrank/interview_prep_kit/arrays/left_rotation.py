def left_rotation(arr, rotations):
    for _ in range(rotations):
        arr.append(arr.pop(0)) 
    return arr


if __name__ == '__main__':
    n, rotations = input().split()
    arr = list(map(int, input().rstrip().split()))

    result = left_rotation(arr, int(rotations))
    print(*result)