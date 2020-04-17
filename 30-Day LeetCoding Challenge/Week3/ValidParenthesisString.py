# https://leetcode.com/problems/valid-parenthesis-string/

from typing import Dict, Tuple


class Solution:

    def checkValidString(self, substring: str) -> bool:
        # setup dynamic programming
        # key is Tuple of (substring, balance)
        self._memo: Dict[Tuple[str, int], bool] = {}

        return self._check_valid_string(substring, 0)

    def _check_valid_string(self, substring: str, balance: int) -> bool:
        """
        Recursive method to determine whether the remaining substring can be completed.
        """

        # check the memoization
        key: Tuple[str, int] = (substring, balance)
        
        if key in self._memo:
            return self._memo[key]

        # empty substring is the end point, if the balance is zero at this point, its valid
        if substring == "":
            return True if balance == 0 else False

        # if balance goes below 0 at any point, its not valid
        if balance < 0:
            return False
            
        # if there are not enough remaining characters to return balance to 0, return false
        if balance > len(substring):
            return False

        # otherwise calculate recursively
        ch = substring[0]
        isValid = None
        
        if ch == '(':
            self._memo[key] = self._check_valid_string(substring[1:], balance + 1)
        elif ch == ')':
            self._memo[key] = self._check_valid_string(substring[1:], balance - 1)
        elif ch == '*':
            self._memo[key] = (self._check_valid_string(substring[1:], balance + 1) 
                               or self._check_valid_string(substring[1:], balance) 
                               or self._check_valid_string(substring[1:], balance - 1))
        else:
            raise Exception("bad input char")

        return self._memo[key]

if __name__ == "__main__":
    print(Solution().checkValidString("*()"))