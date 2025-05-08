from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        ans = [0] * len(nums)

        while left <= right:
            square_left = nums[left] ** 2
            square_right = nums[right] ** 2

            if square_left > square_right:
                ans[index] = square_left
                left += 1
            else:
                ans[index] = square_right
                right -= 1

            index -= 1

        return ans

# Example usage
solution = Solution()
nums = [-4, -1, 0, 3, 10]
result = solution.sortedSquares(nums)
print(result)  # Output: [0, 1, 9, 16, 100]