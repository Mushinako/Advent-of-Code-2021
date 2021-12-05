# Day 05 (Hydrothermal Venture)

## Part 1

`collections.defaultdict` can be an memory-efficient way to keep track of all the
coordinate counts here. After checking whether the `x`- or `y`-coordinates are the same,
we can iterate through all the points covered and add 1 to the counters.

```py
coord_count: defaultdict[_Coord, int] = defaultdict(lambda: 0)
for (x1, y1), (x2, y2) in data:
    # Vertical
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            coord_count[(x1, y)] += 1
        continue
    # Horizontal
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            coord_count[(x, y1)] += 1
        continue
count_gt_1 = [n for n in coord_count.values() if n > 1]
print(len(count_gt_1))
```

## Part 2

The tricky thing here is may be how to identify diagonals. One realization is that for
diagnals from bottom-left to top-right, each step both `x` and `y` adds 1 (e.g.,
`(1, 3)`, `(2, 4)`, `(3, 5)`, etc.), keeping the difference between the `x` and `y` the
same. Those from top-left to bottom right adds 1 to `x` while subtracting 1 from `y`
(e.g., `(2, 5)`, `(3, 4)`, `(4, 3)`), keeping the sum of `x` and `y` constant. These 2
criterias can be used to check for diagonals.

```py
coord_count: defaultdict[_Coord, int] = defaultdict(lambda: 0)
for (x1, y1), (x2, y2) in data:
    # Vertical
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            coord_count[(x1, y)] += 1
        continue
    # Horizontal
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            coord_count[(x, y1)] += 1
        continue
    # Get coordinate's relative positions for diagonals
    if x1 < x2:
        big_x = x2
        small_x = x1
        start_y = y1
    else:
        big_x = x1
        small_x = x2
        start_y = y2
    # Bottom-left to top-right
    if x1 - y1 == x2 - y2:
        for s in range(big_x - small_x + 1):
            coord_count[(small_x + s, start_y + s)] += 1
        continue
    # Top-left to bottom-right
    if x1 + y1 == x2 + y2:
        for s in range(big_x - small_x + 1):
            coord_count[(small_x + s, start_y - s)] += 1
        continue
count_gt_1 = [n for n in coord_count.values() if n > 1]
print(len(count_gt_1))
```
