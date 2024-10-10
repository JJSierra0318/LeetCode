'''

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
            