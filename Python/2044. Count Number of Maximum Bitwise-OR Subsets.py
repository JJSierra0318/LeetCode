'''
Idea is to save every possible subset in the cache that fulfills the condition
then return the length of the cache, it would have been faster to not save anything
and instead have a counter, but this was my first solution and I'll see if I can
optimize it in the future
'''

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        bitOr = reduce(ior, nums)
        cache = []
        
        def dp(i, subset):
            if i >= len(nums):
                return
            subset.append(nums[i])
            if reduce(ior, subset) == bitOr:
                cache.append(subset.copy())
            dp(i + 1, subset)
            subset.pop()
            dp(i + 1, subset)

        dp(0, [])
        return len(cache)
        