# Day 1 b

import numpy as np


class Parser:
    """Parse a file with 2 numbers per line."""

    def __init__(self, fp: str) -> None:
        """
        Initialize the parser with a file path.

        Args:
            fp (str): file path
        """
        with open(fp) as f:
            self.lines = f.readlines()

    def parse(self) -> tuple[np.ndarray, np.ndarray]:
        """Parse the file and return 2 arrays of numbers."""
        arr1 = []
        arr2 = []
        for line in self.lines:
            a, b = line.split()
            arr1.append(int(a))
            arr2.append(int(b))
        return np.array(arr1), np.array(arr2)


def main() -> None:
    """
    Find the sum of the product of the number of occurrences of a
    number from arr1 in arr2.
    """
    p = Parser("in.txt")
    (arr1, arr2) = p.parse()
    sum = 0
    for left in arr1:
        accournce = 0
        for right in arr2:
            if left == right:
                accournce += 1
        sum += accournce * left
    print(sum)


if __name__ == "__main__":
    main()
