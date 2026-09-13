class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)
        for word in strs:
            curr_word = [0] * 26
            for letter in word:
                curr_word[ord(letter) - ord('a')] += 1
            
            tracker[tuple(curr_word)].append(word)

        return list(tracker.values())