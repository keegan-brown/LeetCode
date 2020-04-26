# https://leetcode.com/problems/happy-number/

from typing import Set

class Solution:
    def isHappy(self, n: int) -> bool:
        
        memo: Set[int] = set()

        while n not in memo:
            memo.add(n)
            n = sum([int(digit)**2 for digit in str(n)])
            if n == 1:
                return True
        return False

if __name__ == "__main__":
    print(
        Solution().isHappy(100)
    )