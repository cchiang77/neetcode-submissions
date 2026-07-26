class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, n in enumerate(nums):
            tar = target - n
            if tar in dict:
                return [dict[tar], i]
            dict[n] = i
        