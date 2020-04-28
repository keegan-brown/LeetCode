# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3310/

from typing import List, Sequence

class Solution:

    def canJump(self, nums: List[int]) -> bool:
        """
        Look for zeros, and check if they can be jumped over.
        """
        maxIndex = 0
        i = 0
        n = len(nums)

        while i <= maxIndex < n-1:
            maxIndex = max(maxIndex, i + nums[i])
            i+=1

        if maxIndex >= n-1:
            return True
        return False


    def canJump_brute_force(self, nums: List[int]) -> bool:
        """
        This is a brute force approach. Time limit exceeded
        """
        self._memo = {}
        return self._perform_jump(nums, 0)

    def _perform_jump(self, nums: Sequence[int], idx: int) -> bool:
        
        if idx >= len(nums)-1:
            return True

        if idx in self._memo:
            return self._memo[idx]

        for i in range(nums[idx], 0, -1):
            if self._perform_jump(nums, idx+i):
                self._memo[idx] = True
                return True

        self._memo[idx] = False
        return False

if __name__ == "__main__":
    print(
        Solution().canJump([1, 1, 0, 1])
    )