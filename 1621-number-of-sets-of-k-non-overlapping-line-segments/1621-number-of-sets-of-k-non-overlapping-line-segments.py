class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        r = 2 * k
        x = 1

        for i in range(1, r + 1):
            x = x * (n + k - i) // i

        return x % (10**9 + 7)