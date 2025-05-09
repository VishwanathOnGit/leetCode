def moveZeroes(nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums

# Example usage
nums = [0,1,0,3,12]
result = moveZeroes(nums)
print(result)  # Output: [1,3,12,0,0]