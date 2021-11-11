def plusMinus(arr):
    len_arr = len(arr)
    pos, neg, zero = (0, 0, 0)
    
    for n in arr:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            zero += 1
            
    print("{:.6f}".format(pos/len_arr))
    print("{:.6f}".format(neg/len_arr))
    print("{:.6f}".format(zero/len_arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)