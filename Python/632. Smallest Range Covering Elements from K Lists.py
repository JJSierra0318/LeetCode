'''
The intuition to solve this problem was reached thanks to the following diagram:

[4,10,15,24,26] [0,9,12,20] [5,18,22,30] 0, 5
[4,10,15,24,26] [9,12,20] [5,18,22,30] 4, 9
[10,15,24,26] [9,12,20] [5,18,22,30] 5, 10
[10,15,24,26] [9,12,20] [18,22,30] 9, 18
[10,15,24,26] [12,20] [18,22,30] 10, 18
[15,24,26] [12,20] [18,22,30] 12, 18
[24,26] [20] [18,22,30] 18, 24
[24,26] [20] [22,30] 20, 24
[24,26] [] [22,30]  stop

So basically we keep track of the smallest among the first values of every list and the range
between the smallest and largest value in this list. We save this range in the "smallest" variable,
pop the next heap item and get the next value from the same list as the one we just popped
'''

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq, [nums[i][0], i])
            del nums[i][0]

        maxRange = max(pq)[0]
        smallest = [pq[0][0], maxRange]
        
        while len(pq) == len(nums):
            if not nums[pq[0][1]]:
                break
            maxRange = max(maxRange, nums[pq[0][1]][0])
            heapq.heappush(pq, [nums[pq[0][1]].pop(0), heapq.heappop(pq)[1]])
            if maxRange - pq[0][0] < smallest[1] - smallest[0]:
                smallest = [pq[0][0], maxRange]

        return smallest