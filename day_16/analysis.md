# Day 16 (Packet Decoder)

## Part 1

This is more or less just implementing the rules. There are a few issues to consider
during the implementation:

1. How do we convert the hexadecimal into a binary, while not loosing all the 0's at the
   beginning?
2. How do we keep track of which part of the data we have already read and parsed?

With these 2 issues resolved, we can then parse the data recursively into a tree
structure. Applying the version summation recursively will get the answer.

[\(Solution too big to be embedded\)](solution.py)

## Part 2

Once we got the tree this part is relatively easy. We can just implement the logic for
each packet type using the new [match-case][1] in Python 3.10. :sunglasses:

[\(Solution too big to be embedded\)](solution.py)

[1]: https://www.python.org/dev/peps/pep-0636/
