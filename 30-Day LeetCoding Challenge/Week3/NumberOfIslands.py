# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3302/

from typing import List, Optional, Sequence

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Use an internal 2d map to keep track of points that have been checked. 
        If we encounter fresh land, we should recursively label this with the current island count.
        None = not checked
        0 = water
        1, 2, 3... are separate islands
        """

        # setup internal list, and counter for islands
        self._map: List[List[Optional[int]]] = [[None for x in subgrid] for subgrid in grid]
        self._count_islands: int = 0

        # loop thru all positions, we don't need to check the edges, they are guaranteed to be water
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                # if this point has already been mapped, skip it
                if self._map[i][j] is not None:
                    continue

                # if the point is water, we can mark it and continue
                if grid[i][j] == "0":
                    self._map[i][j] = 0
                    continue

                # if it is an island, we need to mark it and search it, land ahoy!
                if grid[i][j] == "1":
                    self._count_islands += 1
                    self._exploreIsland(grid, i, j)

        return self._count_islands

    def _exploreIsland(self, grid:Sequence[Sequence[str]], i: int, j: int):
        """
        Internal recursive method to search the island
        """

        # check grid boundaries
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return

        # if this point has been mapped, exit this recursive branch
        if self._map[i][j] is not None:
            return

        # if we have stepped into water, we should stop continuing the search
        if grid[i][j] == "0":
            return

        # otherwise mark on map that this point belongs to the current island
        # and take a step in each direction
        self._map[i][j] = self._count_islands
        for ij in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            self._exploreIsland(grid, *ij)

if __name__ == "__main__":
    Solution().numIslands(
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"],
        ])