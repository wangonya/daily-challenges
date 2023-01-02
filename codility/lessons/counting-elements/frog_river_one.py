def solution(X, A):
    x = dict()

    for i,n in enumerate(A):
        if n in x:
            continue

        x[n] = n
        
        if len(x) == X:
            return i

    return -1
        
assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
