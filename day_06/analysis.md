# Day 06 (Lanternfish)

## Part 1

One thing to notice is that we don't really care about an individual lanternfish (sorry
(｡•́︿•̀｡)), we care more about how many lantenrfishes are on each stage each day. The
general idea each day can be summarized as:

1. Take the number of lanternfishes with 0 days left out
2. Move the number of lanternfishes forward (e.g., the number of lanternfishes with 4
   days left become the number of lanternfishes with 3 days left)
3. Set the number of lanternfishes with 8 days left as the 0-day number taken out (this
   is the number of new lanternfishes)
4. Add the 0-day number taken out to the number of lanternfishes with 6 days (this is
   the number of lanterfishes that just created another)

Implemented into code, this looks like:

```py
counts = [0] * 9
for d in data:
    counts[d] += 1
for _ in range(80):
    mature_count = counts.pop(0)
    counts.append(mature_count)
    counts[6] += mature_count
print(sum(counts))
```

## Part 2

Gladly this solution is efficient enough for 256 days!

```py
counts = [0] * 9
for d in data:
    counts[d] += 1
for _ in range(256):
    mature_count = counts.pop(0)
    counts.append(mature_count)
    counts[6] += mature_count
print(sum(counts))
```
