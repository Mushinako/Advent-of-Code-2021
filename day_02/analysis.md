# Day 02 (Dive!)

## Level 1

Implementation! Do what the problem says!

```py
hori = depth = 0
for direction, distance in data:
    if direction == "forward":
        hori += distance
        continue
    if direction == "down":
        depth += distance
        continue
    if direction == "up":
        depth -= distance
        continue
print(hori * depth)
```

## Level 2

Slightly different implementation!

```py
hori = depth = aim = 0
for direction, distance in data:
    if direction == "forward":
        hori += distance
        depth += aim * distance
        continue
    if direction == "down":
        aim += distance
        continue
    if direction == "up":
        aim -= distance
        continue
print(hori * depth)
```
