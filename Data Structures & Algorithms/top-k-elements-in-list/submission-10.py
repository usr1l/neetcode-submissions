class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = defaultdict(int)
        max_freq = 0
        for num in nums:
            tracker[num] += 1

        
        pairs = list(tracker.items())
        freq = [[] for _ in range(len(nums) + 1)]
        for pair in pairs:
            freq[pair[1]].append(pair[0])
        res = []
        for i in range(len(freq)-1, -1, -1):
            if len(freq[i]) > 0 and k > 0:
                while len(freq[i]):
                    res.append(freq[i].pop())
                    k -= 1     

        return res