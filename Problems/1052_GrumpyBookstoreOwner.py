# https://leetcode.com/problems/grumpy-bookstore-owner/

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """
        Solution methodology:
        Use a sliding window, sum of ranges to left and right 
        """

        # edge case: 
        if X == 1 and len(customers) == 1:
            return customers[0]

        # initialise left and right sums, and best score
        # here the window is hard left
        left = 0
        centre = sum(customers[0:X])
        right = sum([customers[i] for i in range(X, len(customers)) if not grumpy[i]==1])
        best = left + centre + right

        # shift window and adjust left and right sums as we move, update best if it changes
        for i in range(1, len(customers) - X + 1):
            
            # adjust left, centre and rights

            # left: if person is not grumpy, add them
            if not grumpy[i-1] == 1:
                left += customers[i-1]

            # centre: everyone is not grumpy, just subtract leaving and add entering
            centre = centre - customers[i-1] + customers[i+X-1]

            # right: if person is not grumpy, subtract them
            if not grumpy[i+X-1] == 1:
                right -= customers[i+X-1]
            
            # update best
            best = max(best, left+centre+right)
            
        return best

if __name__ == "__main__":
    Solution().maxSatisfied([1, 1, 2, 3], [1, 0, 1, 1], 2)