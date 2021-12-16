# pyright: reportMissingTypeStubs=false
""""""

from __future__ import annotations

from functools import reduce
from operator import mul
from typing import TYPE_CHECKING

from utils import SolutionAbstract

if TYPE_CHECKING:
    from typing import Any, TypeAlias

    _Data: TypeAlias = "_Reader"


class Solution(SolutionAbstract):
    day = 16
    data: _Data

    @staticmethod
    def _process_data(raw_data: list[str]) -> _Data:
        """
        Process day 16 data.
        """
        (hex_data,) = raw_data
        # Tried to convert to int and back to binary. Bad mistake. Lost all the
        #   preceding 0's. Instead, parse each letter into 4 binary digits and
        #   concatenate all of them
        bin_data = "".join(f"{int(char, 16):>04b}" for char in hex_data)
        return _Reader(bin_data)

    def part_1(self) -> int:
        """
        Day 16 part 1 solution.
        """
        root_packet = self.parse(self.data)
        return root_packet.get_version_sum()

    def part_2(self) -> int:
        """
        Day 16 part 2 solution.
        """
        root_packet = self.parse(self.data)
        return root_packet.get_value()

    def parse(self, reader: _Reader) -> _Packet:
        """
        Parse packet structure.
        """
        version = int(reader.read(3), 2)
        type_ = int(reader.read(3), 2)

        # Literal value
        if type_ == 4:
            segment = ""
            while True:
                part = reader.read(5)
                segment += part[1:]
                if part[0] == "0":
                    break
            number = int(segment, 2)
            return _Packet(version, type_, number, [])

        # Some operator
        else:
            length_type = reader.read(1)

            # Bit length
            if length_type == "0":
                bit_length = int(reader.read(15), 2)
                target_index = reader.index + bit_length
                children: list[_Packet] = []
                while target_index > reader.index:
                    children.append(self.parse(reader))
                # Sanity check
                if target_index < reader.index:
                    raise ValueError(
                        f"Index mismatch: {target_index=} vs {reader.index=}"
                    )

            # Sub-packet count
            else:
                packet_count = int(reader.read(11), 2)
                children: list[_Packet] = [
                    self.parse(reader) for _ in range(packet_count)
                ]

            return _Packet(version, type_, -1, children)


class _Reader:
    """
    A string reader that keeps track of the last read index.
    """

    def __init__(self, data: str) -> None:
        self.data = data
        self.index = 0

    def read(self, length: int) -> str:
        if length < 0:
            raise ValueError("Cannot read negative length.")
        if length == 0:
            return ""
        if self.index + length > len(self.data):
            raise ValueError("Cannot read past the end of the data.")
        self.index += length
        return self.data[self.index - length : self.index]


class _Packet:
    """
    Packet (node?) object.
    """

    _OPERATION_MAP = {
        0: "sum",
        1: "prod",
        2: "min",
        3: "max",
        5: "gt",
        6: "lt",
        7: "eq",
    }

    def __init__(
        self, version: int, type_: int, value: int, children: list[_Packet]
    ) -> None:
        self.version = version
        self.type_ = type_
        self.value = value
        self.children = children

    def __str__(self) -> str:
        if self.type_ == 4:
            data = f"v{self.version}: {self.value}"
        else:
            data = f"v{self.version} {self._OPERATION_MAP[self.type_]}: {self.children}"
        return f"<{data}>"

    def __repr__(self) -> str:
        return str(self)

    def to_dict(self) -> int | dict[str, list[Any]]:
        """
        Convert to dictionary, to be exported into JSON or pretty printed.
        """
        if self.type_ == 4:
            return self.value
        return {
            self._OPERATION_MAP[self.type_]: [
                child.to_dict() for child in self.children
            ]
        }

    def get_version_sum(self) -> int:
        """"""
        return sum(
            [self.version, *(child.get_version_sum() for child in self.children)]
        )

    def get_value(self) -> int:
        children_values_gen = (child.get_value() for child in self.children)
        match self.type_:
            case 0:
                return sum(children_values_gen)
            case 1:
                return reduce(mul, children_values_gen, 1)
            case 2:
                return min(children_values_gen)
            case 3:
                return max(children_values_gen)
            case 4:
                return self.value
            case 5:
                return int(next(children_values_gen) > next(children_values_gen))
            case 6:
                return int(next(children_values_gen) < next(children_values_gen))
            case 7:
                return int(next(children_values_gen) == next(children_values_gen))
            case invalid:
                raise ValueError(f"Invalid type: {invalid}.")
