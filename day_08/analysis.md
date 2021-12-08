# Day 08 (Seven Segment Search)

## Part 1

1, 4, 7, and 8 can be inferred from segment lengths. Counting all the lengths with
valid values can get the result:

```py
print(sum(len(v) in {2, 3, 4, 7} for _, values in data for v in values))
```

## Part 2

After identifying 1, 4, 7, and 8, we can separate the rest into 5- and 6-segment digits.
2, 3, and 5 are 5-segment digits, and 0, 6, and 9 are 6-segment digits.

* 6: 6-segment, does not encompass 1; helps identifying bottom-right segment
* 0: 6-segment, not 6, does not encompass 4
* 9: 6-segment, not 0 or 6
* 5: 5-segment, encompassed by 6
* 3: 5-segment, encompasses 1
* 2: 5-segment, not 3 or 5

```py
sum_ = 0
for digits, values in data:
    digit_list: list[frozenset[str]] = [frozenset() for _ in range(10)]
    digit_map: dict[frozenset[str], int] = {}
    seg_length_map: dict[int, set[frozenset[str]]] = {
        5: set(),  # 2, 3, 5
        6: set(),  # 0, 6, 9
    }
    # Identify the easy digits
    for d in digits:
        len_ = len(d)
        if len_ == 2:
            digit_list[1] = d
            digit_map[d] = 1
        elif len_ == 3:
            digit_list[7] = d
            digit_map[d] = 7
        elif len_ == 4:
            digit_list[4] = d
            digit_map[d] = 4
        elif len_ == 7:
            digit_list[8] = d
            digit_map[d] = 8
        else:
            seg_length_map[len_].add(d)
    # Identify 0, 6, and 9
    for s6 in seg_length_map[6]:
        if len(s6 & digit_list[1]) == 1:
            digit_list[6] = s6
            digit_map[s6] = 6
        elif len(s6 & digit_list[4]) == 4:
            digit_list[9] = s6
            digit_map[s6] = 9
        else:
            digit_list[0] = s6
            digit_map[s6] = 0
    # Identify 2, 3, and 5
    for s5 in seg_length_map[5]:
        if len(s5 & digit_list[6]) == 5:
            digit_list[5] = s5
            digit_map[s5] = 5
        elif len(s5 & digit_list[1]) == 2:
            digit_list[3] = s5
            digit_map[s5] = 3
        else:
            digit_list[2] = s5
            digit_map[s5] = 2
    sub_sum = 0
    # Calculate sum
    for v in values:
        sub_sum *= 10
        sub_sum += digit_map[v]
    sum_ += sub_sum
print(sum_)
```
