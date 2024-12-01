# Day 1 a

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
        """Parse the file and return 2 arrays of numbers.

        Returns:
            tuple[np.ndarray, np.ndarray]: 2 arrays of numbers
        """
        # accept 2 numbers per line and return 2 arrays of numbers
        arr1 = []
        arr2 = []
        for line in self.lines:
            a, b = line.split()
            arr1.append(int(a))
            arr2.append(int(b))
        return np.array(arr1), np.array(arr2)


def main() -> None:
    """Find the sum of the absolute difference between 2 arrays."""
    p = Parser("in.txt")
    (arr1, arr2) = p.parse()
    # sort arr1 and arr2
    arr1.sort()
    arr2.sort()
    # find the difference between the two arrays per element
    sum = 0
    for i in range(len(arr1)):
        sum += np.abs(arr1[i] - arr2[i])
    print(sum)


if __name__ == "__main__":
    main()
