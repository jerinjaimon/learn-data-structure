"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

"""
class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)  # rows
        n = len(matrix[0])  # column
        result = []
        max_col = n - 1
        max_row = m - 1
        min_col = 0
        min_row = 0
        while min_col <= max_col and max_row >= min_row:
            for i in range(min_col, max_col+1):
                # for j in range(min_row):
                result.append(matrix[min_row][i])
            min_row += 1
            for i in range(min_row, max_row+1):
                result.append(matrix[i][max_col])
            max_col -= 1
            # for row matrix and column matrix
            if not (left < right and bottom > top):
                break
            for i in range(max_col, min_col-1, -1):
                result.append(matrix[max_row][i])
            max_row -= 1
            for i in range(max_row, min_row-1, -1):
                result.append(matrix[i][min_col])
            min_col += 1
        return result
"""


class Solution:
    def spiralOrder(self, matrix):
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and bottom > top:
            # from left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            # for row matrix and column matrix
            if not (left < right and bottom > top):
                break

            # for right to left
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # for whats left in left col
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


s = Solution()
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
