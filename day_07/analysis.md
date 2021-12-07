# Day 07 (The Treachery of Whales)

## Part 1

One simple solution is just to check all possible numbers and see which one is the
minimum:

```py
from math import inf

min_ = min(data)
max_ = max(data)
min_fuel = inf
for t in range(min_, max_):
    fuel = sum(abs(n - t) for n in data)
    if fuel < min_fuel:
        min_fuel = fuel
print(min_fuel)
```

One slightly clever observation is that when the position moves left by 1, all crabs to
the left spend 1 less fuel each, and all crabs to the right spend 1 more fuel each.
Therefore, we want to find a point where an equal number of crabs are on the left and
right side of the position, so that moving the position either left or right will
increase the total fuel cost:

```py
from statistics import median

median_ = round(median(data))
print(sum(abs(n - median_) for n in data))
```

## Part 2

Similar to part 1; can be brute forced:

```py
from math import inf

min_ = min(data)
max_ = max(data)
min_fuel = inf
for t in range(min_, max_):
    fuel = sum(abs(n - t) * (abs(n - t) + 1) // 2 for n in data)
    if fuel < min_fuel:
        min_fuel = fuel
print(min_fuel)
```

This can also be solved somewhat similarly to the median method, but it isn't worth it
given the time constraint.
