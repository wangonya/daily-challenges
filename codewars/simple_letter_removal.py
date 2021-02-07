# https://www.codewars.com/kata/5b728f801db5cec7320000c7

def simple_letter_removal(st, k):
    st_len = len(st)
    st_set = sorted(set(st))
    left_most = st_set[0]
    
    for i in range(k):
        try:
            idx = st.index(left_most)
            if idx+1 == st_len:
                st = st[:idx]
            else:
                st = st[:idx] + st[-st_len+idx+1:]
            st_len = len(st)
        except ValueError:
            st_set.pop(0)
            try:
                left_most = st_set[0]
            except IndexError:
                return ''
            idx = st.index(left_most)
            if idx+1 == st_len:
                st = st[:idx]
            else:
                st = st[:idx] + st[-st_len+idx+1:]
            st_len = len(st)
        
    return st

# best solution from codewars
# def solve(st,k): 
#     for l in sorted(st)[:k]:
#         st=st.replace(l,'',1)
#     return st

assert simple_letter_removal('abracadabra', 1) == 'bracadabra'
assert simple_letter_removal('abracadabra', 2) == 'brcadabra'
assert simple_letter_removal('abracadabra', 6) == 'rcdbr'
assert simple_letter_removal('abracadabra', 8) == 'rdr'
assert simple_letter_removal('abracadabra', 50) == ''