"""
Binary Search.

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""


class Solution:
    def search(self, nums, target: int) -> int:
        """
        # More efficient
        left, right = 0, len(nums) - 1
        while(left <= right):
            pivot = left + (right - left) // 2  # Best to avoid overflow
            if target == nums[pivot]:
                return pivot
            if target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1
        """
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 2))
