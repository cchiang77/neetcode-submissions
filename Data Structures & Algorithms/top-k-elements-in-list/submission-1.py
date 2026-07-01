class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        result = []
        for _ in range(k):
            best_key = None
            best_val = -1
            for key, val in count.items():
                if val > best_val:
                    best_val = val
                    best_key = key
            result.append(best_key)
            del count[best_key]
        
        return result
        