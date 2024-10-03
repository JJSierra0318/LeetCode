'''
While this problem could have been easily resolved using one of python's
libraries like heapq I decided to do it from scratch to get a better
understanding of Heaps
'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0] + sorted(nums)
        self.k = k
        while len(self.heap) - 1 > k:
            self.heap.pop(1)

    def add(self, val: int) -> int:
        if len(self.heap) > self.k:
            if val < self.heap[1]:
                return self.heap[1]
            self.pop()
        self.push(val)
        return self.heap[1]

    def push(self, val: int):
        
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def pop(self):
        if len(self.heap) == 1:
            return
        if len(self.heap) == 2:
            self.heap.pop()
            return

        self.heap[1] = self.heap.pop()
        i = 1
        while 2*i < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
                self.heap[i], self.heap[ 2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)