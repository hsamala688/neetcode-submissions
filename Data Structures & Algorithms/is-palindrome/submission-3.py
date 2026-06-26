class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # go through ignore the spaces hash everything with a count, 
        # then check if for validity by having either a 2 or 1 check, 1 only valid if it is middle index of new string

        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:

            if not s[left].isalnum():
                left += 1
                continue

            elif not s[right].isalnum():
                right -= 1
                continue

            elif s[left] == s[right]:

                left += 1
                right -= 1

            else:

                return False

        return True


        