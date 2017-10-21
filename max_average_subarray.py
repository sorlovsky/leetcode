import math
from functools import reduce
# $[1,12,-5,-6,50,3], k = 4

def average(nums):
    return reduce(lambda x, y: x + y, nums)/len(nums)
    # total = 0
    # for num in nums:
    #     total += num
    # print(total/len(nums))
    # return total/len(nums)



# class Solution1(object):
#     def maxSubArrayLen(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         sums = {}
#         cur_sum, max_len = 0, 0
#         for i in range(len(nums)):
#             cur_sum += nums[i]
#             if cur_sum == k:
#                 max_len = i + 1
#             elif cur_sum - k in sums:
#                 max_len = max(max_len, i - sums[cur_sum - k])
#             if cur_sum not in sums:
#                 sums[cur_sum] = i  # Only keep the smallest index.
#         return max_len

class Solution:
    # def __init__():

    # def findMaxAverage(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: float
    #     """
    #     max_sub = -500
    #     for i in range(k, len(nums)+1):
    #         # print(nums[i-k:i])
    #         if average(nums[i-k:i]) > max_sub:
    #             max_sub = average(nums[i-k:i])
    #         # print(i)
    #     # if len(nums) == 1:
    #     #   return nums[0]
    #     return max_sub
    def findMaxAverage(self, A, k):
        max_ending_here = max_so_far = A[0:k]
        for x in A[k:]:
            print(x)
            list(max_ending_here).append(x)
            print(max_ending_here)
            list(max_ending_here) = max(x, average(max_ending_here))
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
# print(s.maxSubArrayLen([5], 1))
# print(s.maxSubArrayLen([0,1,1,3,3], 4))