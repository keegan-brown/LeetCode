from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        # build left and right multiple arrays
        left:   List[int] = [None] * n
        right:  List[int] = [None] * n

        # initialise left array
        left[0]     = 1
        right[n-1]  = 1

        for i in range(1, n):
            left[i]         = left[i-1] * nums[i-1]
            right[n-1-i]    = right[n-i] * nums[n - i]

        return [x*y for x, y in zip(left, right)]
        
if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))
