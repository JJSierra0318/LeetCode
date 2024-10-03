'''
Reached an initial solution that worked but constanty got TLE:

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0
        i, j = 0, 1
        n = len(nums)
        counter = n
        nums = [x % p for x in nums]
        for i in range(n):
            total = 0
            for j in range(i, n):
                total = (nums[j] + total) % p
                if total == remainder and j - i + 1 < counter:
                    counter = j - i + 1
        if counter == n:
            return - 1
        return counter

After reading some hints I understood I had to look for a solution
with one loop using mod and a map. We will only check for the mod.
Initial logic is, if we find a substring of mods which sum results
in the remainder of the total sum of the array (remainder = sum(nums) % p)
and then remove said substring the problem will be solved.

For that, every cumulative mod is saved in a dictionary as a key with the last
index as its value, if we find the same key when checking if the current sum
would suffice the remainder then it means that the sum of all the numbers between
both indexes result in the remainder and are a viable subset to remove

The las step is to check if the differce of both indexes is less than the current
counter, which starts as the maximun being the length of the array, as we want to
find the shortest subarray to remove.

Some final notes:
dic = {0: -1}
- is initialized in zero to account for when we dont need to remove anything

if dic.get((total - remainder + p) % p) is not None:
- "+ p" is optional, and only there so operations remain positive, it works
the same without it
- we check if there is key/value pair thath contains what total is missing to
  add up to the remainder

counter = min(counter, i - dic[(total - remainder + p) % p])
- we substrack i and the value found on the dictionary as both represents positions
  and by doing so we would find the total length in which the sum adds up to remainder

'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0
        n = len(nums)
        counter = n
        dic = {0: -1}
        total = 0
        for i in range(n):
            total = (total + nums[i]) % p
            if dic.get((total - remainder + p) % p) is not None:
                counter = min(counter, i - dic[(total - remainder + p) % p])
            dic[total] = i
        return counter if counter < n else -1