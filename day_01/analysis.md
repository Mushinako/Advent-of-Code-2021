# Day 01 (Sonar Sweep)

## Part 1

This question can be brute forced: iterate through the list, and compare it with the
next element, and count the number of occurrences where the next number is larger than
the previous.

The slightly tricky part is to figure out how many times to loop. We have to stop at the
second-to-last element because the last element won't have a number after it to compare
with, yielding a total number of loops of `len(data) - 1`.

With that, there're a few different ways to solve it. Here're a few solutions:

```py
counter = 0
prev = data[0]
for d in data[1:]:
    if d > prev:
        counter += 1
    prev = d
print(counter)
```

```py
counter = 0
for i in range(len(data) - 1):
    if data[i+1] > data[i]:
        counter += 1
print(counter)
```

```py
counter = 0
i = 0
while True:
    try:
        if data[i+1] > data[i]:
            counter += 1
    except IndexError:
        break
    i += 1
print(counter)
```

```py
from itertools import
counter = 0
for i in count(0):
    try:
        if data[i+1] > data[i]:
            counter += 1
    except IndexError:
        break
print(counter)
```

```py
import sys

sys.setrecursionlimit(2500)


def calculate_increases(data: list[int], counter: int) -> int:
    if len(data) < 2:
        return counter
    if data[1] > data[0]:
        counter += 1
    return calculate_increases(data[1:], counter)

print(calculate_increases(data, 0))
```

```py
print(sum(data[i + 1] > data[i] for i in range(len(data) - 1)))
```

```py
print(sum(next_ > prev for prev, next_ in zip(data[:-1], data[1:])))
```

## Part 2

The brute force way is to sum up all length-3 sliding windows and comparing them, but
that's no fun. One crucial discovery is that when comparing the windows, 2 of them can
be cancelled out:

```text
d[0] + d[1] + d[2] <?> d[1] + d[2] + d[3]
```

is the same as

```text
d[0]               <?>               d[3]
```

With this discovery, we can now realize that this is basically checking how many numbers
are larger than the number 3 before them. Similar code as **Level 1** applies.
