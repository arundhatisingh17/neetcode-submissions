class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = len(matrix[0])
        b = len(matrix)

        left = 0
        right = l * b - 1

        while left <= right:
            mid = (left + right) // 2

            # convert the middle element to a row_idx, col_idx
            row_idx = mid // l
            col_idx = mid % l

            if matrix[row_idx][col_idx] == target:
                return True

            elif target < matrix[row_idx][col_idx]:
                right = mid - 1
            
            elif target > matrix[row_idx][col_idx]:
                left = mid + 1

        return False