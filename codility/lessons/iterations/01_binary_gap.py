def solution(n):
    n = f'{n:b}'
    _count = 0
    _max = 0
    for i in n:
        if i == '0':
            _count += 1
        else:
            _max = max(_max, _count)
            _count = 0
    return _max
