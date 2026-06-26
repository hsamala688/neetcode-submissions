class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_freq = {}
        left = 0
        max_freq = 0
        length = 0
        
        for i in range(len(s)):

            char_freq[s[i]] = char_freq.get(s[i], 0) + 1

            max_freq = max(max_freq, char_freq[s[i]])

            while (i - left + 1) - max_freq > k:
                
                char_freq[s[left]] -= 1
                left += 1

            length = max(length, i - left + 1)

        return length
