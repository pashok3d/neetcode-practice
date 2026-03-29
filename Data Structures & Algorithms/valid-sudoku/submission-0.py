class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_items: dict[int, set[int]] = defaultdict(set)
        col_items: dict[int, set[int]] = defaultdict(set)
        box_items: dict[int, set[int]] = defaultdict(set)
        
        def get_box_index(row_i, col_i) -> int:
            """
            (0, 0) -> (0, 0) -> 0
            (2, 2) -> (0, 0) -> 0
            (3, 2) -> (1, 0) -> 1
            (3, 3) -> (1, 1) -> 4
            (6, 6) -> (2, 2) -> 8
            (8, 8) -> (2, 2) -> 8
            """
            box_row_i = row_i // 3 
            box_col_i = col_i // 3 
            return 3 * box_row_i + box_col_i

        for row_i, row in enumerate(board):
            for col_i, item in enumerate(row):
                if item == ".":
                    continue
                if item in row_items[row_i]:
                    print("1", row_i, col_i)
                    return False
                if item in col_items[col_i]:
                    print("2", row_i, col_i)
                    return False
                box_id = get_box_index(row_i, col_i)

                if item in box_items[box_id]:
                    print("3", row_i, col_i)
                    return False

                row_items[row_i].add(item)
                col_items[col_i].add(item)
                box_items[box_id].add(item)

        return True
                