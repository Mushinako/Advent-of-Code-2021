# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations


def solution(data: tuple[list[int], list[list[list[int]]]]) -> int:
    """
    Day 04 part 1 solution.
    """
    numbers, num_boards = data
    sel_boards = [[[False] * 5 for _ in range(5)] for _ in num_boards]
    for n in numbers:
        for b, num_board in enumerate(num_boards):
            for i, num_row in enumerate(num_board):
                for j, num_cell in enumerate(num_row):
                    if num_cell == n:
                        sel_boards[b][i][j] = True
        for b, sel_board in enumerate(sel_boards):
            if _check_bingo(sel_board):
                return n * sum(
                    num_cell
                    for num_row, sel_row in zip(num_boards[b], sel_board)
                    for num_cell, sel_cell in zip(num_row, sel_row)
                    if not sel_cell
                )
    # Make linter happy
    return 0


def _check_bingo(board: list[list[bool]]) -> bool:
    return any(all(row) for row in board) or any(all(col) for col in zip(*board))
