"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much
as every other number in the array. If it is, return the index of the largest
element, or return -1 otherwise.


Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number
because there are no other numbers.
"""


class Solution:
    def dominantIndex(self, nums: list) -> int:
        largest_num = sorted(nums, reverse=True)[0]
        idx = nums.index(largest_num)
        for i, item in enumerate(nums):
            if i != idx and largest_num < 2*item:
                return -1
        return idx


# s = Solution()
# print(s.dominantIndex([3, 6, 1, 0]))
