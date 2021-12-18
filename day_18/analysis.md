# Day 18 (Snailfish)

## Part 1

Another tree implementation. The main methods on the nodes would be getting magnitude
recursively, and checking and executing explosion and splitting. To restart the process
after each explosion/splitting, I utilized an exception to immediately return to the top
loop.

[\(Solution too big to be embedded\)](solution.py)

## Part 2

Very similar to the first one, with the difference of having to permute all possible
combinations. One thing to note is that because we may be doing operations on the nodes
and mutating them, making a deep copy that maintains the relationships properly is
crucial.

[\(Solution too big to be embedded\)](solution.py)
