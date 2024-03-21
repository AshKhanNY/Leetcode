class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Idea I have in mind is HashSets, where we'd add values
        # to the set and if there are any duplicates, we return false
        # Set would be a representation of the rule of 1-9 only for
        # each box. It looks like we ONLY care about dupes in 3x3s
        # EDIT: Nvm we consider rows and cols too. Added 2 more set
        # lists for those as well
        rm = 0
        cm = 0
        boxes = [set() for _ in range(9)]
        rows  = [set() for _ in range(9)]
        cols  = [set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                i = ((cm // 3) % 3) + ((rm // 3) * 3)
                if val in boxes[i]:
                    return False
                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                if (val != "."):
                    boxes[i].add(val)
                    rows[r].add(val)
                    cols[c].add(val)
                cm += 1
            rm += 1
        return True
