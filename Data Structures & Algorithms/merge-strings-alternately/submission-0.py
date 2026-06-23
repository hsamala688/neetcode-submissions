class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ""
        total_len = len(word1) + len(word2)
        count = 0

        w1 = 0
        w2 = 0

        while count < total_len:
            if w1 >= len(word1):
                result += word2[w2]
                w2 += 1
                count += 1
            elif w2 >= len(word2):
                result += word1[w1]
                w1 += 1
                count += 1
            else:
                result += word1[w1]
                w1 += 1
                result += word2[w2]
                w2 += 1
                count += 2
        
        return result