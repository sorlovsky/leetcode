def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    prev_num = -1
    duplicate = -1

    def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

    l = list(range(1, len(nums)+1))
    missing_num = diff(l, nums)[0]

    for num in nums:
        if prev_num == num:
            duplicate = num
        prev_num = num
    return duplicate, missing_num

# nums = [1,2,2,4]
nums = [2,2]
print(findErrorNums(nums))