'''
Using backtracking we check the maximum length of two options, either we add the
current string to the list of substrings or we add another char to the string,
additionally, if the current substring is already in the list, then we only want to
check adding another char to the string, as we can't add it to the list of substrings.

When we finally get to the end, we return the length of the list which will be compared
by the first recursive call
'''

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def recursion(i, substring, substrings):
            if i == len(s):
                return len(substrings)
            substring += s[i]
            if substring in substrings:
                return recursion(i + 1, substring, substrings)
            return max(recursion(i + 1, '', substrings + [substring]), recursion(i + 1, substring, substrings))
        return recursion(0, '', [])