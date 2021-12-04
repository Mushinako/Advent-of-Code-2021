# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: tuple[list[int], list[list[list[int]]]]) -> int:
    """
    Day 04 part 2 solution.
    """
    numbers, num_boards = data
    sel_boards = [[[False] * 5 for _ in range(5)] for _ in num_boards]
    # Make linter happy
    result = 0
    for n in numbers:
        for b, num_board in enumerate(num_boards):
            for i, num_row in enumerate(num_board):
                for j, num_cell in enumerate(num_row):
                    if num_cell == n:
                        sel_boards[b][i][j] = True
        new_board_nums: list[list[list[int]]] = []
        new_boards: list[list[list[bool]]] = []
        for b, sel_board in enumerate(sel_boards):
            board_num = num_boards[b]
            if _check_bingo(sel_board):
                result = n * sum(
                    num_cell
                    for num_row, sel_row in zip(board_num, sel_board)
                    for num_cell, sel_cell in zip(num_row, sel_row)
                    if not sel_cell
                )
            else:
                new_board_nums.append(board_num)
                new_boards.append(sel_board)
        num_boards = new_board_nums
        sel_boards = new_boards
    return result


def _check_bingo(board: list[list[bool]]) -> bool:
    return any(all(row) for row in board) or any(all(col) for col in zip(*board))
