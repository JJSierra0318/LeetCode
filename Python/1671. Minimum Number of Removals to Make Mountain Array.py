'''
The idea es to find the LIS and LDS for every item in the array, the longest
LIS + LDS will be the top of the mountain array so we can find the number of
removals by subtracting this to the total length of the array
'''
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # rev will be used to find LDS, keeping in mind that LDS is ths
        # same as running LIS from right to left
        rev = nums[::-1]
        # We initialize both arrays to 1, as it's the default and minimum
        # LIS possible form any given index
        LIS = [1] * len(nums)
        LDS = [1] * len(nums)
        # We iterate over every index, checking LIS up to every index
        for i in range(1, len(nums)):
          # And we check every number that comes before the given i
            for j in range(i):
                # for LIS we check if the current num is greater than
                # a previous one and if incrementing the count would
                # be greater than with the current number
                if nums[i] > nums[j] and LIS[i] < LIS[j] + 1:
                    LIS[i] = LIS[j] + 1
                # we do the same for LDS, using the reversed list
                if rev[i] > rev[j] and LDS[i] < LDS[j] + 1:
                    LDS[i] = LDS[j] + 1
        # we reverse LDS as it's the result of the reversed list
        LDS = LDS[::-1]
        # init res to 0
        res = 0
        # we check for every item in both LIS and LDS
        for i in range(len(LIS)):
            # we ignore 1s as it wouldn't be an acceptable top of the mountain
            # and we check if the length of the array with top *i* is greater
            if LIS[i] != 1 and LDS[i] != 1 and res < LIS[i] + LDS[i] - 1:
                res = LIS[i] + LDS[i] - 1
        # currenty res has the longest mountain array, so we only have to substract
        # it from the original array to find the minimum about of changes
        return len(nums) - res