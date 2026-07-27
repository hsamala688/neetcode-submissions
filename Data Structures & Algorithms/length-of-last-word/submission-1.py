class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end, length = len(s) - 1, 0
        
        while s[end] == ' ':
            end -= 1

        while end >= 0 and s[end] != ' ':
            end -= 1
            length += 1
        return length