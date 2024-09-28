class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1

        while L <= R:
            mid = (L + R) // 2
            if target < matrix[mid][0]:
                R = mid - 1
            elif target > matrix[mid][-1]:
                L = mid + 1
            else:
                L, R = 0, len(matrix[mid]) - 1
                while L <= R:
                    midn = (L + R) // 2
                    if target < matrix[mid][midn]:
                        R = midn - 1
                    elif target > matrix[mid][midn]:
                        L = midn + 1
                    else:
                        return True
                return False