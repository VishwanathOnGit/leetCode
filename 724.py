def pivotIndex(nums):
    # for i in range(len(nums)):
    #     left_sum = sum(nums[:i])
    #     right_sum = sum(nums[i+1:])
    #     if left_sum == right_sum:
    #         return i
    # return -1 

    left_sum, right_sum = 0, sum(nums)
    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1


print(pivotIndex([1,7,3,6,5,6]))  # Output: 3
print(pivotIndex([1,2,3]))  # Output: -1
print(pivotIndex([2,1,-1]))  # Output: 0