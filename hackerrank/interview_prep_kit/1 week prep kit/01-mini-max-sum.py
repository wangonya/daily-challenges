def miniMaxSum(arr):
    arr.sort()
    arr_sum = sum(arr)
    print(arr_sum-arr[-1], arr_sum-arr[0])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
