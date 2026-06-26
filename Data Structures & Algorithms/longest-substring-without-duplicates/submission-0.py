class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding window problem that is dynamic

        char_freq = {}
        left = 0
        max_len = 0

        for i in range(len(s)):

            char_freq[s[i]] = char_freq.get(s[i], 0) + 1

            while char_freq[s[i]] > 1:

                char_freq[s[left]] -= 1
                left += 1

            max_len = max((i - left + 1), max_len)

        return max_len
            








