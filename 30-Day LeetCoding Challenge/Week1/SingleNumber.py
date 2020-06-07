# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/

from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        
        singles = set()
        for num in nums:
            if num not in singles:
                singles.add(num)
            else:
                singles.remove(num)

        return singles.pop()

if __name__ == "__main__":
    print(
        Solution().singleNumber([1,1,3,2,2])
        )