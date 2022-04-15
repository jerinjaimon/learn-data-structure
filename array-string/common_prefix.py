"""
Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = ""
        idx = 0
        length = len(strs)
        first_word = strs[0]
        if length == 1:
            return first_word
        if first_word != "":
            intermediate = first_word[idx]
            while(idx < len(first_word)):
                f = 0
                for i in range(1, length):
                    if not(strs[i].startswith(intermediate)):
                        f = 1
                        break
                if f == 1:
                    break
                else:
                    idx += 1
                    prefix = intermediate
                    if idx < len(first_word):
                        intermediate += first_word[idx]
                    else:
                        break
        return prefix


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
