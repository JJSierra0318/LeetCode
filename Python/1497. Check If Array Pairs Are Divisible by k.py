class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        res = [0] * k
        for num in arr:
            res[num % k] += 1
        if res[0] % 2 != 0:
            return False
        for i in range(len(res) // 2):
            if res[i + 1] != res[len(res) - i - 1]:
                return False
        return True