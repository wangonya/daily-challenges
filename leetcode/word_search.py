from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_index, row in enumerate(board):
            for cell_index, cell in enumerate(row):
                if cell == word[0]:
                    x=word[0]
                    for char in word[1:]:
                        print(f"row index = {row_index}")
                        print(f"cell index = {cell_index}")
                        if cell_index < len(row) and char == row[cell_index+1]:
                            x+=char
                        elif row_index < len(board) and char == board[row_index+1][cell_index]:
                            x+=char
        print(x)

s = Solution()
assert s.exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED") is True
assert s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE") is True
assert s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB") is False


# Time:  O(m * n * 4 * 3^(l - 1)) ~= O(m * n * 3^l), l is the length of the word
# Space: O(l)

class Solution(object):
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existRecu(board, word, 0, i, j, visited):
                    return True

        return False

    def existRecu(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i - 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i, j + 1, visited) or\
                 self.existRecu(board, word, cur + 1, i, j - 1, visited)
        visited[i][j] = False

        return result
