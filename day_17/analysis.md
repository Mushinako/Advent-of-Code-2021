# Day 17 (Trick Shot)

## Part 1

The nice thing about this question is that we can consider x- and y-axes independently.
For this part, after sufficiently large number of steps, the movement on the x-axis will
stop due to drag. Because we want to get the highest height, we would want to get the
maximum number of steps possible, and therefore it's same to assume that the x-axis
movement will be 0 at the end and can be ignored.

One interesting thing to note on the y-axis is that the positions are roughly
symmetrical when the probe goes up initially. Taking intial y-speed 3 as an example:

```py
   y
 6 |        +1 x 0 x
   |       x        -1 x
 4 |    +2              -2
   |   x                   x
 2 |                        -3
   |+3
 0 x---------------------------x-----time
   |                            -4
-2 |
   |
-4 |                               x
```

(Note that the horizontal axis is not x-axis value. It is a time unit. x-value is not
used here because bringing drag into the conversation makes this unnecessarily
complicated)

After some steps, the probe goes back to the starting y-level and keeps going down, with
a speed of `-3 - 1`. The maximum height here is `3 + 2 + 1 = 3 * (3 + 1) / 2 = 6`.
Therefore, to maximize the height, we need a large initial speed `s`. However, we still
have to make sure that `-s - 1` does not exceed the minimum allowed y-level. We can
thusly set `-s - 1` to minimum allowed level to get the largest `s`.

```py
-s - 1 = min_y => s = -min_y - 1
max_height = s * (s + 1) // 2
           = (-min_y - 1) * (-min_y - 1 + 1) // 2
           = (-min_y - 1) * (-min_y) // 2
```

Proper Python code would look like:

```py
# I did the negation during data processing so no need to negate here
y_depth = self.data[1][1]
print(y_depth * (y_depth - 1) // 2)
```

## Part 2

Again here we can consider x- and y-axes independently.

TODO (Anyone who reads this remind me to fill this in later. Thx)

```py
(x_min, x_max), (y_min, y_max) = self.data

# [Will overshoot?][Min step count]
x_counts: dict[bool, defaultdict[int, set[int]]] = {
    True: defaultdict(set), False: defaultdict(set)
}
for x_end in count(1):
    if x_end > x_max:
        break
    x_acc = 0
    for x in count(x_end):
        x_acc += x
        if x_acc > x_max:
            break
        if x_acc >= x_min:
            x_counts[x_end > 1][x - x_end + 1].add(x)

# [Min step count]
y_counts: defaultdict[int, set[int]] = defaultdict(set)
for y_start in count(1):
    if y_start > y_max:
        break
    y_acc = 0
    for y in count(y_start):
        y_acc += y
        if y_acc > y_max:
            break
        if y_acc >= y_min:
            base_y_step = y - y_start + 1
            y_counts[base_y_step].add(-y_start)
            y_counts[base_y_step + y_start * 2 - 1].add(y_start)

all_starts: set[tuple[int, int]] = set()
# For ones that won't overshoot, as long as the y step count is no smaller than
#   x step count then it's OK
for x_min_step, x_vecs in x_counts[False].items():
    for y_min_step, y_vecs in y_counts.items():
        if y_min_step < x_min_step:
            continue
        all_starts |= {(x, y) for x in x_vecs for y in y_vecs}
# For ones that will overshoot, we need to get exact step count
for x_min_step, x_vecs in x_counts[True].items():
    y_vecs = y_counts.get(x_min_step)
    if not y_vecs:
        continue
    all_starts |= {(x, y) for x in x_vecs for y in y_vecs}

print(len(all_starts))
```
