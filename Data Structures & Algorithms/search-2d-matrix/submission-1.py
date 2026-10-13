class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            l = 0
            r = len(matrix[row]) - 1
            
            while l <= r:
                mid = (l+r) // 2

                if target > matrix[row][mid]:
                    l = mid + 1
                
                if target < matrix[row][mid]:
                    r = mid - 1 
                
                if target == matrix[row][mid]:
                    return True

        return False
        