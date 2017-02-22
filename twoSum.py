'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


EXAMPLE:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
# test


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            total = nums[i] + nums[j]
            if i != j and total == target:
                return [i, j]


def main():
    print(twoSum([1, 3, 5], 4))

main()


