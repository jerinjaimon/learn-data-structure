"""
Given an integer numRows, return the first numRows of Pascal's triangle.

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]
"""


class Solution:
    def generate(self, numRows: int):
        results = []
        inter = [1]
        results.append(inter)
        for i in range(1, numRows):
            if i == 1:
                inter = [1, 1]
                results.append(inter)
            else:
                s = []
                for idx in range(0, len(inter)-1):
                    s1 = inter[idx]+inter[idx+1]
                    s.append(s1)
                inter = [1]+s+[1]
                results.append(inter)
        return results


s = Solution()
print(s.generate(5))
