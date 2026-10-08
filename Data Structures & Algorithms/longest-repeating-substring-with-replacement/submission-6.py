class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_len = 0
        start = 0
        max_freq = 0

        for i in range(len(s)):
            freq[s[i]] += 1

            max_freq = max(max_freq, freq[s[i]])

            while 1 + i - start - max_freq > k:
                freq[s[start]] -= 1
                start+=1

            max_len = max(max_len, 1 + i - start)

        return max_len
