from itertools import groupby

def find_max_consecutive_ones(nums):
    ones = [list(g) for k, g in groupby(nums) if k == 1]
    return len(max(ones)) if ones else 0

# optimal speed solution:
#         lenght=len(nums)
#         zero_counts=nums.count(0)
#         cnt,idx=[],-1
#         for i in range(zero_counts):
#             tem=idx
#             idx=nums.index(0,idx+1,lenght)
#             cnt.append(idx-tem-1)
#         cnt.append(lenght-idx-1)
#         if len(cnt)>0:
#             return max(cnt)
#         return 0

# optimal memory solution:
#         cntSoFar = 0
#         maxOverall = 0
#         for num in nums:
#             if num == 1:
#                 cntSoFar += 1
#                 maxOverall = max(maxOverall, cntSoFar)
#             else:
#                 cntSoFar = 0
#         return maxOverall