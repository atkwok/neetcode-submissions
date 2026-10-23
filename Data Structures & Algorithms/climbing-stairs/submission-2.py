class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        ans = [0, 1, 2, 3]
        for i in range(4, n + 1):
            ans.append(ans[-1] + ans[-2])
        return ans[-1]

