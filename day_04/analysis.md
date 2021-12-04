# Day 04 (Giant Squid)

## Part 1

Loop and loop and loop and loop. Brute force implementation works because the input is
not very big

```py
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
            print(
                n * sum(
                    num_cell
                    for num_row, sel_row in zip(num_boards[b], sel_board)
                    for num_cell, sel_cell in zip(num_row, sel_row)
                    if not sel_cell
                )
            )
            # Exit
```

## Part 2

Basically the same thing, but instead of getting the first valid board, get the last
valid board

```py
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
print(result)
```
