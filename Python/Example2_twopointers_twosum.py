def twosum(nums, target):
    # Set the starting and ending pointers to the first and last elements of the list.
    left = 0
    right = len(nums) - 1

    # Iterate until the left pointer is less than the right pointer, which means we have checked all pairs.
    # If the sum of the elements at the left and right pointers is equal to the target, return True.
    # If the sum is less than the target, move the left pointer one step to the right.
    # If the sum is greater than the target, move the right pointer one step to the left.
    # If we reach this point, it means no pairs sum to the target, so return False.
    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

# Example usage
nums = [1, 2, 4, 6, 8, 9, 14, 15]
nums1 = [1, 7, 11, 15]
target = 13

print(twosum(nums, target))  # Output: True
print(twosum(nums1, target)) # Output: False
