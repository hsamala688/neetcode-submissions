class Solution:
        
        # go through ignore the spaces hash everything with a count, 
        # then check if for validity by having either a 2 or 1 check, 1 only valid if it is middle index of new string
        '''
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
        '''

        def alphaNum(self, c):

            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        def isPalindrome(self, s: str) -> bool:

            left, right = 0, len(s) - 1

            while left < right:

                while left < right and not self.alphaNum(s[left]):

                    left += 1

                while left < right and not self.alphaNum(s[right]):

                    right -= 1

                if s[left].lower() != s[right].lower():

                    return False

                left, right = left + 1, right - 1

            return True

        

        