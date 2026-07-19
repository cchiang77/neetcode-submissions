class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(float(p) / mid)
            if total_hours <= h:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res
