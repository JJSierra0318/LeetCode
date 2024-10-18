'''
There are two solutions, the first one is full math, where we calculate the combination all
the possible combinations with the formula N!/r!(N-r)! where N would be all the possible paths
(so all right m - 1 + all down n - 1) and r are the possible choices (so m-1 or n-1), with some
math the formula ends up being (m + n - 2)! / (m - 1)! * (n - 1)!
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))

'''
However, this was an excercise to practice dp, so I tried this approach aswell, the general idea is
to create a matrix where the first row and col where "1" (representing the amount steps, and because
its the beginning that would the only choices) and then every cell would be equal to the one to the
left + the one above, representing all the paths available to reach that cell, and the last cell will
represent all possible combinations
''' 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] + [0] * (n - 1) for i in range(m - 1)]
        matrix.insert(0, [1] * n)
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]