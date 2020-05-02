class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        R, C = len(matrix), len(matrix[0])
        cr, cc = 0, C - 1
        while cr < R and cc >= 0:
            if matrix[cr][cc] == target:
                return True
            elif matrix[cr][cc] > target:
                cc -= 1
            elif matrix[cr][cc] < target:
                cr += 1
            