class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix[0]) - 1
        row = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                row = i
        if row == -1:
            return False

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] == target:
                return True
        
        return False
