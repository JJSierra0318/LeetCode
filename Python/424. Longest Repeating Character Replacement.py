'''
we create a hashmap with all uppercase letters initialized to 0, and
then start a sliding window approach, where we increment the size of the
window every iteration, and decrease it only if the current amount of
characters that would have to be changed exceeds k, then we move our
Left pointer and subtract one from the count of the current letter
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        characters = {}
        for char in abc:
            characters[char] = 0
        maxAmount = 0
        L = 0
        for R in range(len(s)):
            characters[s[R]] += 1
            amount = characters[s[R]]
            maxAmount = max(maxAmount, amount)
            if (R - L + 1) - maxAmount > k:
                characters[s[L]] -= 1
                L += 1
        return R - L + 1