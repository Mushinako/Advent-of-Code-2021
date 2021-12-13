# Day 13 (Transparent Origami)

## Part 1

A "folding" is essentially a coordinate transformation. The dots below the folding
coordinate (above the y-axis folds and to the left of the x-axis folds) aren't changed.
Those above the folding coordinate (below the y-axis folds and to the right of the x-
axis folds) undergo some form of transition.

Taking `y=7` fold as an example. The `y=8` coordinates are folded onto `y=6`, `y=9` ones
folded onto `y=5`, etc. In general, we get the distance between current line `y` and
folding line `y'` to get `d = y' - y`. Then we can get the reflected line as the line
same distance below it, as `y - d = y - (y' - y) = 2 * y - y'`

```py
def _fold_paper(dots: set[_Coord], axis: str, index: int) -> set[_Coord]:
    """
    Fold the paper once.
    """
    new_dots: set[_Coord] = set()
    for x, y in dots:
        if axis == "x":
            new_dots.add((x if x < index else 2 * index - x, y))
        else:
            new_dots.add((x, y if y < index else 2 * index - y))
    return new_dots

dots, folds = data
axis, index = folds[0]
dots = fold_paper(dots, axis, index)
print(len(dots))
```

## Part 2

Same thing, just that this time we're running it to the end. Parsing the result
programmatically can be a challenge, so I opted for just printing it out and input it
manually.

```py
def _fold_paper(dots: set[_Coord], axis: str, index: int) -> set[_Coord]:
    """
    Fold the paper once.
    """
    new_dots: set[_Coord] = set()
    for x, y in dots:
        if axis == "x":
            new_dots.add((x if x < index else 2 * index - x, y))
        else:
            new_dots.add((x, y if y < index else 2 * index - y))
    return new_dots

dots, folds = data
for axis, index in folds:
    dots = _fold_paper(dots, axis, index)
# Make visual
max_x, max_y = map(max, zip(*dots))
board: list[list[str]] = [[" "] * (max_x + 1) for _ in range(max_y + 1)]
for x, y in dots:
    board[y][x] = "█"
print("\n".join("".join(row) for row in board))
```
