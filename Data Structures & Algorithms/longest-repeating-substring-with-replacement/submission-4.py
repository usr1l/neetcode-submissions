class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        longest_s = 0
        start = 0
        max_freq = 0

        for i in range(len(s)):
            freq[s[i]] += 1
            max_freq = max(max_freq, freq[s[i]])

            if 1 + i - start - max_freq > k:
                freq[s[start]] -= 1
                start += 1
            
            longest_s = max(longest_s, 1 + i - start)

        return longest_s