class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        k = R
        while L <= R:
            mid = (L + R) // 2
            hours = 0
            for num in piles:
                hours += math.ceil(num / mid)
            if hours <= h:
                R = mid - 1
                k = mid
            else:
                L = mid + 1
        return k