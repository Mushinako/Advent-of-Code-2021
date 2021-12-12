# Day 12 (Passage Pathing)

## Part 1

First(?) path finding problem of this year's AoC! A simple [depth-first search][1] can
do the job. Here, it's implemented using recursion.

The caves are firstly mapped into nodes in a graph, and the search is triggered from the
start node end ends at the end node. To keep track of the visited nodes, a set is used
to take advantage of the O(1) access time.

```py
start_node, end_node = data

def path_count(node: _Node, visited_nodes: set[_Node]) -> int:
    """
    Recursion depth-first path-finder.
    """
    # Found a path!
    if node == end_node:
        return 1
    # Don't allow small node to be visited twice
    if node in visited_nodes and not node.is_large:
        return 0
    # Sum all path counts from connected nodes
    return sum(
        path_count(next_node, {node, *visited_nodes}) for next_node in node.connections
    )

print(path_count(start_node, set()))
```

## Part 2

Very similar. There're 2 main changes:

1. Logic change when a small cave is visited twice
   1. If the small cave is the start, stop
   2. If another cave is visited twice, stop
   3. If neither of the above are true, continue
2. Add a boolean flag to keep track of whether a small cave is visited twice

```py
start_node, end_node = data

def path_count(
    node: _Node, visited_nodes: set[_Node], small_visited_twice: bool
) -> int:
    """
    Recursion depth-first path-finder.
    """
    # Found a path!
    if node == end_node:
        return 1
    # Conditionally don't allow small node to be visited twice
    if node in visited_nodes and not node.is_large:
        # Stop if start node or another node is visited twice
        if node == start_node or small_visited_twice:
            return 0
        # Mark this node as visited twice
        small_visited_twice = True
    # Sum all path counts from connected nodes
    return sum(
        path_count(next_node, {node, *visited_nodes}, small_visited_twice)
        for next_node in node.connections
    )

print(path_count(start_node, set()))
```

[1]: https://en.wikipedia.org/wiki/Depth-first_search
