class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = 1
        curMax = 1

        for n in nums:
            temp = curMax * n
            curMax = max(curMin * n, curMax * n, n)
            curMin = min(curMin * n, temp, n)
            res = max(curMax, curMin, res)

        return res
            
        