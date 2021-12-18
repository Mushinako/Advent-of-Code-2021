# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

import json
import logging
from copy import deepcopy
from itertools import permutations
from pathlib import Path
from typing import TYPE_CHECKING, overload

from utils import SolutionAbstract

if TYPE_CHECKING:
    from typing import Any, Literal

    _Data = list["_Node"]

# Logging is commented out in the actual code because of the huge overhead. Turn them
#   back on when needed
_LOGGER = logging.getLogger("day_18")
_LOGGER.setLevel("DEBUG")
_LOG_PATH = Path(__file__).parent / "day_18.log"
_LOG_FH = logging.FileHandler(_LOG_PATH, "w")
_LOG_FH.setLevel("DEBUG")
_LOGGER.addHandler(_LOG_FH)


class Solution(SolutionAbstract):
    day = 18
    data: _Data

    @staticmethod
    def _process_data(raw_data: list[str]) -> _Data:
        """
        Process day 18 data.
        """
        # It's technically not JSON but it is valid JSON ¯\_(ツ)_/¯
        return [_Node.from_list(json.loads(data)) for data in raw_data]

    def part_1(self) -> int:
        """
        Day 18 part 1 solution.
        """
        result = self.data[0]
        data = self.data[1:]
        # Add then reduce
        for add in data:
            result += add
            # _LOGGER.debug(f"After addition: {result}")
            # Continue reducing until there're no reductions
            while True:
                try:
                    result.reduce_explode()
                    result.reduce_split()
                except _NextIteration:
                    # _LOGGER.debug(f"After reduction: {result}")
                    continue
                else:
                    break
            # _LOGGER.debug(f"Finished reduction: {result}")
        return result.calc_magnitude()

    def part_2(self) -> int:
        """
        Day 18 part 2 solution.
        """
        max_ = 0
        # Calculate all possible permutations and find a max
        for x, y in permutations(self.data, 2):
            # Deep copy is required because we're going to manipulate the node during
            #   reduction. Data in `self.data` may be modified without deep copy because
            #   they're referenced in the result
            result = deepcopy(x + y)
            # Continue reducing until there're no reductions
            while True:
                try:
                    result.reduce_explode()
                    result.reduce_split()
                except _NextIteration:
                    continue
                else:
                    break
            magnitude = result.calc_magnitude()
            # _LOGGER.debug(f"{x=}, {y=}: {magnitude=}")
            max_ = max(max_, magnitude)
        return max_


class _Node:
    """
    Number nodes.

    Args:
        left (int | _Node):
            Left node.
        right (int | _Node):
            Right node.
        position (None | "left" | "right"):
            The node position in the parent node. `None` if no parent node is present.
        parent (Node | _Node):
            Parent node. `None` if the current node is the root node.

    Attributes:
        position (None | "left" | "right"):
            The node position in the parent node. `None` if no parent node is present.
        parent (Node | _Node):
            Parent node. `None` if the current node is the root node.

    Properties:
        left (int | _Node; get & set):
            Left node.
        right (int | _Node; get & set):
            Right node.
    """

    parent: None | _Node
    position: None | Literal["left", "right"]
    _left: int | _Node
    _right: int | _Node

    def __init__(
        self,
        left: _Node | int,
        right: _Node | int,
        position: None | Literal["left", "right"] = None,
        parent: None | _Node = None,
    ) -> None:
        self._left = -1
        self._right = -1
        self.left = left
        self.right = right
        self.position = position
        self.parent = parent

    def __deepcopy__(self, memo: dict[Any, Any]) -> _Node:
        """
        Convert to list and parse again to easily make a value copy of the node instead
          of just another reference.
        """
        return _Node.from_list(self.to_list())

    @property
    def left(self) -> int | _Node:
        """
        Left child node.
        """
        return self._left

    @left.setter
    def left(self, value: int | _Node) -> None:
        """
        Setting a left child node also updates the child's `position` and `parent`.
        """
        self._left = value
        if isinstance(value, _Node):
            value.position = "left"
            value.parent = self

    @property
    def right(self) -> int | _Node:
        """
        Right child node.
        """
        return self._right

    @right.setter
    def right(self, value: int | _Node) -> None:
        """
        Setting a right child node also updates the child's `position` and `parent`.
        """
        self._right = value
        if isinstance(value, _Node):
            value.position = "right"
            value.parent = self

    @overload
    @classmethod
    def from_list(cls: type[_Node], data: int, position: ..., parent: ...) -> int:
        ...

    @overload
    @classmethod
    def from_list(
        cls: type[_Node],
        data: list[Any],
        position: None | Literal["left", "right"] = None,
        parent: None | _Node = None,
    ) -> _Node:
        ...

    @classmethod
    def from_list(
        cls: type[_Node],
        data: int | list[Any],
        position: None | Literal["left", "right"] = None,
        parent: None | _Node = None,
    ) -> int | _Node:
        """
        Parse the input nested list into a node structure.

        Args:
            data (int | list):
                The nested list data. If the data is a number, then we're already at
                the lowerest level and the number is returned directly. Else, parse the
                nested list into a tree structure.
            position (None | "left" | "right"):
                The node position in the parent node. `None` if no parent node is
                present.
            parent (Node | _Node):
                Parent node. `None` if the current node is the root node.
        """
        if isinstance(data, int):
            return data
        left, right = data
        node = cls(-1, -1, position, parent)
        node.left = cls.from_list(left, "left", node)
        node.right = cls.from_list(right, "right", node)
        return node

    def to_list(self) -> list[Any]:
        """
        Represent the node as a nested list of numbers, just like the input.

        Returns:
            (list):
                A list of 2 elements: the left and right nodes. Each child node will be
                the value if the value is a number, else convert the child node to a
                list recursively
        """
        left = self.left
        right = self.right
        return [
            left if isinstance(left, int) else left.to_list(),
            right if isinstance(right, int) else right.to_list(),
        ]

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"

    def __repr__(self) -> str:
        return f"Node({self.left},{self.right})"

    def __add__(self, o: object) -> _Node:
        if isinstance(o, (int, _Node)):
            return _Node(self, o)
        return NotImplemented

    def __radd__(self, o: object) -> _Node:
        if isinstance(o, (int, _Node)):
            return _Node(o, self)
        return NotImplemented

    @property
    def nest_level(self) -> int:
        """
        Get the nest level. If the nest level >4 the node may need to be exploded.
        """
        level = 1
        node = self
        while node.parent is not None:
            node = node.parent
            level += 1
        return level

    def calc_magnitude(self) -> int:
        """
        Calculate magnitude recursively.

        Returns:
            (int): Calculated magnitude.
        """
        left = self.left
        left_value = left if isinstance(left, int) else left.calc_magnitude()
        right = self.right
        right_value = right if isinstance(right, int) else right.calc_magnitude()
        return 3 * left_value + 2 * right_value

    def _get_left_neighbor(self) -> None | tuple[_Node, Literal["left", "right"]]:
        """
        Get the left neighbor node from current node. Used in `explode`.

        Returns:
            (None | (_Node, ("left" | "right"))):
                `None` if no left neighbor is present. A tuple of `(node, position)` if
                one exists. The `node` is the parent node and `position` is the position
                of the neighbor. The actual node is a number so we have to get the
                parent and position.
        """
        # Go up
        node = self
        while True:
            if node.parent is None:
                return None
            if node.position == "left":
                node = node.parent
                continue
            elif node.position == "right":
                node = node.parent
                break
        # Go down
        if isinstance(node.left, int):
            return node, "left"
        node = node.left
        while not isinstance(node.right, int):
            node = node.right
        return node, "right"

    def _get_right_neighbor(self) -> None | tuple[_Node, Literal["left", "right"]]:
        """
        Get the right neighbor node from current node. Used in `explode`.

        Returns:
            (None | (_Node, ("left" | "right"))):
                `None` if no right neighbor is present. A tuple of `(node, position)` if
                one exists. The `node` is the parent node and `position` is the position
                of the neighbor. The actual node is a number so we have to get the
                parent and position.
        """
        # Go up
        node = self
        while True:
            if node.parent is None:
                return None
            if node.position == "right":
                node = node.parent
                continue
            elif node.position == "left":
                node = node.parent
                break
        # Go down
        if isinstance(node.right, int):
            return node, "right"
        node = node.right
        while not isinstance(node.left, int):
            node = node.left
        return node, "left"

    def explode(self) -> None:
        """
        Explode the current node.
        """
        if self.position is None:
            raise ValueError("Cannot explode top level node.")
        # Add left value to the left neighbor
        left_neighbor = self._get_left_neighbor()
        if left_neighbor is not None:
            left_node, left_position = left_neighbor
            setattr(
                left_node, left_position, getattr(left_node, left_position) + self.left
            )
        # Add right value to the right neighbor
        right_neighbor = self._get_right_neighbor()
        if right_neighbor is not None:
            right_node, right_position = right_neighbor
            setattr(
                right_node,
                right_position,
                getattr(right_node, right_position) + self.right,
            )
        # Remove current node
        setattr(self.parent, self.position, 0)
        del self

    def split(self, position: Literal["left", "right"]) -> None:
        """
        Split the number on the left/right position of the node.

        Args:
            position ("left" | "right"):
                Position of node to be splitted.
        """
        value: int | _Node = getattr(self, position)
        # Check to make sure the child node to be splitted is actually an number
        if isinstance(value, _Node):
            raise ValueError("Cannot split a node.")
        setattr(self, position, _Node(value // 2, (value + 1) // 2, position, self))

    def reduce_explode(self) -> None:
        """
        Recursively check for potential explosions and explode them.
        """
        # _LOGGER.debug(f"Checking explode: {self}")
        left_int = isinstance(self.left, int)
        right_int = isinstance(self.right, int)
        # Reached deepest level & nesting count >4. Explode and restart
        if left_int and right_int and self.nest_level > 4:
            # _LOGGER.debug(f"Exploding: {self}")
            self.explode()
            raise _NextIteration
        # This node all good. Check children
        if not left_int:
            self.left.reduce_explode()
        if not right_int:
            self.right.reduce_explode()

    def reduce_split(self) -> None:
        """
        Recursively check for potential splittings and split them.
        """
        # _LOGGER.debug(f"Checking split: {self}")
        left_int = isinstance(self.left, int)
        right_int = isinstance(self.right, int)

        # Check if left number is too big, if it's a number
        if left_int:
            if self.left >= 10:
                # _LOGGER.debug(f"Spliting left: {self}")
                self.split("left")
                raise _NextIteration
        # Check left children
        else:
            self.left.reduce_split()

        # Check if right number is too big, if it's a number
        if right_int:
            if self.right >= 10:
                # _LOGGER.debug(f"Spliting right: {self}")
                self.split("right")
                raise _NextIteration
        # Check right children
        else:
            self.right.reduce_split()


class _NextIteration(Exception):
    """
    Special exception to indicate that either an explosion or a splitting has happened
      so that we can start again from the top level.
    """
