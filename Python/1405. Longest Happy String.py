'''
Idea is to keep track of the letter with the most amount of letters with a heap
but if it would break the rule of not three consecutive of the same we remove it
temporarily from the heap to evaluate the next letter. We break if we run out of
letters or the only other option is to brek the rule
'''

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [[-a, "a"], [-b, "b"], [-c, "c"]]
        heapq.heapify(heap)
        if heap[2][0] == 0:
            del heap[2]
        if heap[1][0] == 0:
            del heap[1]
        
        res = ""
        count = 0
        while len(heap) >= 1 and count < 2:
            temp = None
            if res and heap[0][1] == res[-1]:
                count += 1
                if count == 2:
                    if len(heap) == 1:
                        break
                    temp = heapq.heappop(heap)
                    count = 0
            res += heap[0][1]
            heap[0][0] += 1
            if heap[0][0] >= 0:
                heapq.heappop(heap)
            if temp:
                heapq.heappush(heap, temp)

        return res