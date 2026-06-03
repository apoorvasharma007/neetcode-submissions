class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        row_pointer = 0
        col_pointer = 0

        for row_pointer in range(rows):
            first_elem = matrix[row_pointer][0]
            last_elem = matrix[row_pointer][-1]

            if first_elem <= target <= last_elem:
                left = 0
                right = cols-1
                while(left<=right):
                    mid = math.floor((left + right) / 2)
                    curr_elem = matrix[row_pointer][mid]
                    if curr_elem == target:
                        return True
                    elif curr_elem < target:
                        left = mid + 1 
                    else:
                        right = mid - 1
            else: 
                row_pointer += 1

        return False