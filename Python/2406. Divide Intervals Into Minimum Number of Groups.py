'''
Sort by arrival and create an empty heap called groups which will store the end
of the interval of the current group. If the start of the next interval lesser than
the current end, then all of the groups would intersect as the current one is the lowest
end value so we "create" a new group by appending the value to the heap. If the start is
greater than the current end, then there would not be an intersection so we remove the
current end and add the end of the interval, simulating and update for the current group
'''

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups = []

        for start, end in intervals:
            if groups and groups[0] < start:
                heapq.heappop(groups)
            heapq.heappush(groups, end)

        return len(groups)                   