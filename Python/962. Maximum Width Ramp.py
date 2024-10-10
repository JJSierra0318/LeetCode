'''
Had a previous solution that got a TLE but I got lost as I didn't understand the
concept of a monotonic stack, so after some reading I understood we wanted the
lowest "i" possible with the biggest "j" possibe aslong as i <= j, so with a stack
such as [1, 2, 2, 2, ...] we only care about the "1" as any number that satisfies
the solution with two (2 <= x) will also be satisfied with the one as 1 <= 2 and is
the leftmost item, however if we got [2, 1, 2, 2, ...] we should consider both as
there's a chance x >= 2, in which case 2 also satisfies the solution and it's more
to the left than the "1".

The final example that helped me understand the logic was [2, 3, 1, 2, ...], in this
case, every case that could use the "3" can also be used by the "2" to the left and
it will have a bigger width ramp, so we should only consider [2, 1], which means we
can create a stack going left to right where we only append values if they're less
than the current top of the stack. This will represent all possible starts of the
ramp.
'''

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(nums)):
            if len(stack) == 0 or nums[i] < stack[-1][0]:
                stack.append((nums[i], i))
        
        for i in range(len(nums) -1, 0, -1):
            while len(stack) > 0 and stack[-1][0] <= nums[i]:
                res = max(res, i - stack.pop()[1])
        
        return res
            