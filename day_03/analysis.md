# Day 03 (Binary Diagnostic)

## Part 1

The easiest way to treat individual digits is probably just to treat it as a string.
Utilizing Python's `collections.Counter`, we can efficiently determine which digit is
more common. At the end, `int(number, 2)` converts the binary string into a proper
number.

```py
gamma_str = ""
epsilon_str = ""
for digits in zip(*data):
    counter = Counter(digits)
    common_order = counter.most_common()
    gamma_str += common_order[0][0]
    epsilon_str += common_order[-1][0]
print(int(gamma_str, 2) * int(epsilon_str, 2))
```

## Part 2

Very similar to part 1 in terms of the core logic. Still bit comparison,
`collections.Counter` still very helpful, and still `int(number, 2)` at the end. One
potentially tricky part is the tie breaker, where `1` is treated as more common in case
of a tie. For that, we can sort the list in reverse to take advantage of the fact that
`collections.Counter` treats the first seen value as more common in case of a tie.

```py
# Data is sorted in decending order to make sure that 1's are always at the front and
#   therefore will always be returned as the most common one in the case of a tie
data.sort(reverse=True)
length = len(data[0])
# Careful not to modify the original data
o2_values = data
for i in range(length):
    if len(o2_values) == 1:
        break
    o2_counter = Counter(d[i] for d in o2_values)
    most_common = o2_counter.most_common(1)[0][0]
    o2_values = [d for d in o2_values if d[i] == most_common]
# Careful not to modify the original data
co2_values = data
for i in range(length):
    if len(co2_values) == 1:
        break
    co2_counter = Counter(d[i] for d in co2_values)
    least_common = co2_counter.most_common()[-1][0]
    co2_values = [d for d in co2_values if d[i] == least_common]
print(int(o2_values[0], 2) * int(co2_values[0], 2))
```
