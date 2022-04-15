"""
Diagonal Traverse.

Given an m x n matrix mat, return an array of all the elements of the array
in a diagonal order.

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""


class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        result = [[] for i in range(m+n-1)]
        out = []
        for i in range(n):
            for j in range(m):
                result[i+j].append(mat[j][i])
        for i, item in enumerate(result):
            if i % 2 != 0:
                item.reverse()
            [out.append(e) for e in item]
        return out


# s = Solution()
# print(s.findDiagonalOrder([[1, 2], [3, 4]]))
