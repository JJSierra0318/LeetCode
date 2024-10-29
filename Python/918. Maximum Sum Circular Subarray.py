'''
We use Kadane's with a twist, we also save the minimum subarray, considering that
it's a circular array there are two possible answers: the biggest subarray if it's
contained inside the flat initial array or the total - the minimum subarray, which
would remove the minimum sum if it's somewhere in the middle of the array
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # keep track of both the maximum and minimum sum subarray
        sumMax, sumMin = nums[0], nums[0]
        # current max sum, min sum and total sum
        currMax, currMin, total = 0, 0, 0
        for num in nums:
            # always add to the total sum
            total += num
            # we add the minimum current and updated the sum
            currMin = min(num, currMin + num)
            sumMin = min(currMin, sumMin)
            # same with the maximum
            currMax = max(num, currMax + num)
            sumMax = max(currMax, sumMax)
        # as explained above, there are two options, return the maximum sum or the total minus
        # the minimum, this will be determined by which one is larger
        return sumMax if total - sumMin < sumMax or total - sumMin == 0 else total - sumMin