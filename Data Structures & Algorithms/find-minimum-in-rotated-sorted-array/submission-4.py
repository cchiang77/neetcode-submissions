class Solution: 
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] < nums[j]:
                i += 1
                j += 1
            elif nums[i] > nums[j]:
                return nums[j]
        return nums[0]