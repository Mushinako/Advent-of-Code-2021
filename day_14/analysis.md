# Day 14 (Extended Polymerization)

## Part 1

This problem is essentially a more complicated version of [Lanternfish][1]. The trick
here is to consider pairs of letters, and how they split into two pairs of letters. For
example, for the rule `CH -> B`, the pair `CH` got split into pairs `CB` and `BH`.
Utilizing this we can get a pretty efficient solution.

One thing to note is that when converting pairs of letter counts to single letter
counts, *almost* all letters are counted twice. E.g., for the letters `ABCD`, we count
the occurrences of `AB`, `BC`, and `CD`. Therefore, `B` and `C` are counted twice. The
exceptions are the characters at the end of the string, in this case `A` and `D`, which
are only counted once. To get the counts for the characters, we'll have to add 1 to the
counts of the 2 letters on the sides, and divide the counts by 2.

```py
template, rules = data

def _solve( step_count: int) -> int:
    """
    General solution.
    """
    counts = {position: 0 for position in rules}
    for i in range(len(template) - 1):
        counts[template[i : i + 2]] += 1
    for _ in range(step_count):
        counts = _run_step(counts)
    char_counts = _get_char_counts(counts)
    counts_list = sorted(char_counts.items(), key=itemgetter(1), reverse=True)
    return counts_list[0][1] - counts_list[-1][1]

def _run_step(counts: dict[str, int]) -> dict[str, int]:
    """
    Run one step.
    """
    new_counts = {position: 0 for position in counts}
    for position, count in counts.items():
        value = rules.get(position)
        if not value:
            continue
        new_counts[position[0] + value] += count
        new_counts[value + position[1]] += count
    return new_counts

def _get_char_counts(pair_counts: dict[str, int]) -> dict[str, int]:
    """
    Get character count from pair count.
    """
    char_counts = {char: 0 for char in (set(template) | set(rules.values()))}
    for position, count in pair_counts.items():
        char_counts[position[0]] += count
        char_counts[position[1]] += count
    char_counts[template[0]] += 1
    char_counts[template[-1]] += 1
    for char, count in char_counts.items():
        if count % 2:
            raise ValueError(f"{char!r} does not have an even count: {count}.")
    char_counts = {char: count // 2 for char, count in char_counts.items()}
    return char_counts

print(_solve(10))
```

## Part 2

Gladly the solution for part 1 is efficient enough to be used for 40 steps!

```py
template, rules = data

def _solve( step_count: int) -> int:
    """
    General solution.
    """
    counts = {position: 0 for position in rules}
    for i in range(len(template) - 1):
        counts[template[i : i + 2]] += 1
    for _ in range(step_count):
        counts = _run_step(counts)
    char_counts = _get_char_counts(counts)
    counts_list = sorted(char_counts.items(), key=itemgetter(1), reverse=True)
    return counts_list[0][1] - counts_list[-1][1]

def _run_step(counts: dict[str, int]) -> dict[str, int]:
    """
    Run one step.
    """
    new_counts = {position: 0 for position in counts}
    for position, count in counts.items():
        value = rules.get(position)
        if not value:
            continue
        new_counts[position[0] + value] += count
        new_counts[value + position[1]] += count
    return new_counts

def _get_char_counts(pair_counts: dict[str, int]) -> dict[str, int]:
    """
    Get character count from pair count.
    """
    char_counts = {char: 0 for char in (set(template) | set(rules.values()))}
    for position, count in pair_counts.items():
        char_counts[position[0]] += count
        char_counts[position[1]] += count
    char_counts[template[0]] += 1
    char_counts[template[-1]] += 1
    for char, count in char_counts.items():
        if count % 2:
            raise ValueError(f"{char!r} does not have an even count: {count}.")
    char_counts = {char: count // 2 for char, count in char_counts.items()}
    return char_counts

print(_solve(40))
```

[1]: ../day_06/analysis.md
