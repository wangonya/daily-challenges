

# This is a demo task.

# Write a function:

#     class Solution { public int solution(int[] A); }

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].

from typing import List

def solution(A: List):
    missing = 0
    A.sort()

    if A[-1] < 0:
        return 1

    for i in range(len(A)-1):
        if A[i] < 0:
            continue

        if A[i+1] - A[i] != 1:
            missing = A[i]+1

    if missing == 0:
        missing = A[-1] + 1

    print(missing)
    return missing

assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1, 3, 2]) == 4
assert solution([-1, -3]) == 1


