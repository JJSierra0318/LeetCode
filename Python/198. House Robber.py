'''
With dynamic programming we save the current amount of money and
the previous one, if adding the current house with the prev results
in more money, then thats the new result and the previously maximun
becomes prev which will be checked against the next house on the
next iteration
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        res, prev = 0, 0
        for num in nums:
            prev, res = res, max(num + prev, res)
        return res