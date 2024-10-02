'''
Logic revolves around deciding to include or not include the next value, when we have an inital list of [1],
the two options are to include it and continue ([1, 2]) or not include it and continue ([2]), and then for
each option another two options are created ([1, 2, 3] and [1, 3]) for the first one and ([2, 3] and [3])
for the second one. The cycle continues until we reach the end of the original list
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def perm(num: int, subset: List[int] = []):
            if num >= len(nums):
                return
            
            subset.append(nums[num])
            res.append(subset[:])
            perm(num + 1, subset)
            subset.pop()
            perm(num + 1, subset)
        
        perm(0)
        return res
