# Day 4 part 2

import logging
from typing import List

logging.basicConfig(level=logging.INFO)


def check_XMAS(data: List[List[str]], i: int, j: int) -> bool:
    """Check if an X-MAS pattern is present at the center (i, j).

    Args:
        data (List[List[str]]): The data to search in
        i (int): The row index
        j (int): The column index

    Returns:
        bool: True if an X-MAS pattern is found, False otherwise
    """
    # Check bounds for the 3x3 area
    if i - 1 < 0 or i + 1 >= len(data) or j - 1 < 0 or j + 1 >= len(data[0]):
        return False

    # Define valid X-MAS patterns
    patterns = [
        [
            ["M", None, "S"],
            [None, "A", None],
            ["M", None, "S"],
        ],
        [
            ["S", None, "M"],
            [None, "A", None],
            ["S", None, "M"],
        ],
        [
            ["M", None, "M"],
            [None, "A", None],
            ["S", None, "S"],
        ],
        [
            ["S", None, "S"],
            [None, "A", None],
            ["M", None, "M"],
        ],
    ]

    # Check each pattern
    for pattern in patterns:
        match = True
        for pi, row in enumerate(pattern):
            for pj, char in enumerate(row):
                if char is not None and data[i - 1 + pi][j - 1 + pj] != char:
                    match = False
                    break
            if not match:
                break
        if match:
            return True

    return False


def search_XMAS(data: List[List[str]]) -> int:
    """Search for all X-MAS patterns in the data.

    Args:
        data (List[List[str]]): The data to search in

    Returns:
        int: The number of X-MAS patterns found
    """
    occurrences = 0

    # Iterate through the grid, treating each cell as the center of a potential X-MAS
    for i in range(len(data)):
        for j in range(len(data[0])):
            if check_XMAS(data, i, j):
                occurrences += 1

    return occurrences


def main() -> None:
    # Read input data
    try:
        with open("in.txt") as f:
            raw_data = f.read()  # Read raw data
    except FileNotFoundError:
        logging.error("Input file 'in.txt' not found.")
        return

    # Prepare data
    lines = raw_data.strip().split("\n")  # Split into lines
    data: List[List[str]] = [list(row) for row in lines]  # Convert to List[List[str]]

    # Search for X-MAS patterns
    total_occurrences = search_XMAS(data)

    print(f"Total occurrences of X-MAS: {total_occurrences}")
    return None


if __name__ == "__main__":
    main()
