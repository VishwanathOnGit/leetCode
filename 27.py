def removeElement(nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Test cases
print(removeElement([3,2,2,3], 3))  # Output: 2
print(removeElement([0,1,2,2,3,0,4,2], 2))  # Output: 5
print(removeElement([1,2,3,4,5], 6))  # Output: 5
print(removeElement([1,2,3,4,5], 1))  # Output: 4
print(removeElement([1,1,1,1,1], 1))  # Output: 0