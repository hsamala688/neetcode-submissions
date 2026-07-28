class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (s == "" and t != "") or (s != "" and t == ""):
            return False

        count_S = {}
        count_T = {}

        for char in s:
            count_S[char] = count_S.get(char, 0) + 1

        for char in t:
            count_T[char] = count_T.get(char, 0) + 1

        return count_S == count_T