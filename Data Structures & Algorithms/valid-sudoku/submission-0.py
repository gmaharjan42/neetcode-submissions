class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #checks for duplicates across rows
        for row in range(9):
            seenNums = set()
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seenNums:
                    return False
                seenNums.add(num)

        #checks if duplicates are in columns
        for col in range(9):
            seenNums = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seenNums:
                    return False
                seenNums.add(num)

        #check 3x3 blocks
        for startRow in [0, 3, 6]:
            for startCol in [0, 3, 6]:
                seenNums = set()
                for row in range(startRow, startRow + 3):
                    for col in range(startCol, startCol + 3):
                        num = board[row][col]
                        if num == ".":
                            continue
                        if num in seenNums:
                            return False
                        seenNums.add(num)
        return True




        #rows will go through indices 0-8, 9-17, 18-26, etc.

        #columns will go through indices differently (top down), so
        #0,9,18,27 etc...

        #will need helper function to create 3x3 matrix blocks and will need
        #to check this block for duplicates as well
        