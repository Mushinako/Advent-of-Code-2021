# Day 10 (Syntax Scoring)

## Part 1

For each closing character, it should match the last open character. One thing we can do
is to put all the open characters on a [stack][1]. This allows easier pushing and
popping of the last character. In Python, a list does this job quite well:

```py
pair_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
sum_ = 0
for line in data:
    stack: list[str] = []
    for char in line:
        if char in pair_map:
            stack.append(char)
        else:
            last_open = stack.pop()
            correct_char = pair_map[last_open]
            if char != correct_char:
                sum_ += score_map[char]
                break
print(sum_)
```

## Part 2

After filtering out all the broken lines, the closing characters needed to be added each
line can be found by getting the corresponding character for each opening characters
popped from the stack:

```py
from statistics import median

pair_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
score_map = {"(": 1, "[": 2, "{": 3, "<": 4}
scores: list[int] = []
for line in data:
    stack: list[str] = []
    for char in line:
        if char in pair_map:
            stack.append(char)
        else:
            last_open = stack.pop()
            correct_char = pair_map[last_open]
            # Broken line
            if char != correct_char:
                break
    else:
        # All checked, no broken
        sub_total = 0
        for char in reversed(stack):
            sub_total *= 5
            sub_total += score_map[char]
        scores.append(sub_total)
print(int(median(scores)))
```

[1]: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
