class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        min_len = float('inf')
        min_str = ""

        for i in range(len(t)):
            letter = t[i]
            t_dict[letter] += 1
        
        matches = len(t_dict)

        start, end = 0, 0

        while end < len(s):
            letter = s[end]
            s_dict[letter] += 1

            if s_dict[letter] == t_dict[letter]:
                matches -= 1

            end += 1

            while matches == 0 and (end - start + 1) >= len(t):
                if (end-start+1) < min_len:
                    min_len = min(min_len, (end - start + 1))
                    min_str = s[start:end]
                letter = s[start]
                s_dict[letter] -= 1

                if s_dict[letter] < t_dict[letter]:
                    matches += 1

                start += 1

        return min_str