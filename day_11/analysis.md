# Day 11 (Dumbo Octopus)

## Part 1

Another careful implementation. What else can I say other than following the logic?

[\(Solution too big to be embedded\)](solution.py)

## Part 2

The main running logic is the same. The only difference is that we'll need to check
when all octopi flash together. In my implementation, I have a hashset `flashed` that
keeps track of all flashed octopi, and I can just check its length. An alternative is
to loop through the grid and check to make sure all octopi are at stage 0.

[\(Solution too big to be embedded\)](solution.py)
