class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    box_idx = (r // 3, c // 3)
                    if (r, val) in seen or (val, c) in seen or (box_idx, val) in seen:
                        return False
                    seen.add((r, val))
                    seen.add((val, c))
                    seen.add((box_idx, val))
        return True
