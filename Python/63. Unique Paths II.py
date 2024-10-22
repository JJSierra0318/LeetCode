'''
At any given point, the amount of possible paths is the sum of the paths from
the right and from the top, in this case, if an obstacle is found then the 
possible paths in that specific spot would be zero. for the inital case,
(first row and first column) if an obstacle is foun then it isn't possible
to reach any position beyond that  obstacle, so after this all positions
should have zero possible paths (handled by a flag)
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # If an obstacle is found at the start or the beginning, then there 
        # aren't any paths
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        # For the first row, if we find an obstacle, all other positions to
        # right are unreachable
        foundObs = False
        prevRow = []
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                foundObs = True
            if foundObs:
                prevRow.append(0)
            else:
                prevRow.append(1)
        
        # We reset the flag to use it once again with the cols
        foundObs = False
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                foundObs = True
            row = [0] if foundObs else [1]
            # With the first row and col handled it's only a matter
            # of adding the previous paths to the current position
            # if there isn't any obstacle
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    row.append(0)
                else:
                    row.append(row[-1] + prevRow[j])
            prevRow = row
        return prevRow[-1]