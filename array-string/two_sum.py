"""
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as
an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.
We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.
We return [1, 2].
"""


class Solution:
    def twoSum(self, numbers, target: int):
        # for idx, item in enumerate(numbers):
        #     for i in range(idx+1, len(numbers)):
        #         s = item+numbers[i]
        #         if s == target:
        #             return [idx+1, i+1]

        start, end = 0, len(numbers)-1

        while start < end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start+1, end+1]

            if s < target:
                start += 1
            if s > target:
                end -= 1


s = Solution()
print(s.twoSum([5, 25, 75], 100))
