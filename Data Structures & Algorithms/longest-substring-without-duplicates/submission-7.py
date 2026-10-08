class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_tracker = defaultdict()
        longest_len = 0
        str_start = 0


        for i in range(len(s)):
            if s[i] not in str_tracker or str_tracker[s[i]] < str_start:
                longest_len = max(longest_len, i - str_start + 1)

            else:
                str_start = str_tracker[s[i]] + 1
            
            str_tracker[s[i]] = i
                
        return longest_len