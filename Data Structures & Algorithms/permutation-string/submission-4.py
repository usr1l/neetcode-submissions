class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_letters = defaultdict(int)
        s2_letters = defaultdict(int)
        start, end = 0, len(s1) - 1
        matches = 0

        for i in range(len(s1)):
            s1_letters[s1[i]] += 1
        
        matches = len(s1_letters)

        for j in range(0, len(s1)):
            s2_letters[s2[j]] += 1

            if s2_letters[s2[j]] == s1_letters[s2[j]]:
                matches -= 1

            elif s2_letters[s2[j]] == s1_letters[s2[j]] + 1:
                matches += 1
        
        while end < len(s2):
            if matches == 0:
                return True
            if end >= len(s2) - 1:
                break
            
            s2_letters[s2[start]]-=1

            if s2_letters[s2[start]] == s1_letters[s2[start]]:
                matches-=1

            elif s2_letters[s2[start]] == s1_letters[s2[start]] - 1:
                matches += 1

            s2_letters[s2[end+1]]+=1

            if s2_letters[s2[end+1]] == s1_letters[s2[end+1]]:
                matches -=1
            
            elif s2_letters[s2[end+1]] == s1_letters[s2[end+1]] + 1:
                matches += 1

            start += 1
            end += 1

        return False
