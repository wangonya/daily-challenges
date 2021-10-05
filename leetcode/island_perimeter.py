from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row, squares in enumerate(grid):
            for col, square in enumerate(squares):
                if square == 1:
                    perimeter += 4
                    if row != 0 and grid[row - 1][col] == 1:
                        perimeter -= 2
                    if col != 0 and grid[row][col - 1] == 1:
                        perimeter -= 2

        return perimeter


s = Solution()
assert s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
assert s.islandPerimeter([[1]]) == 4
assert s.islandPerimeter([[1, 0]]) == 4
