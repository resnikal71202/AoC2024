# Day 4 part 1

import logging
from typing import List

logging.basicConfig(level=logging.INFO)


def check_XMAS(data: List[List[str]], i: int, j: int, dr: int, dc: int) -> bool:
    """Check if the word 'XMAS' is present starting at (i, j) in a given direction.

    Args:
        data (List[List[str]]): The data to search in
        i (int): The starting row index
        j (int): The starting column index
        dr (int): The row direction
        dc (int): The column direction

    Returns:
        bool: True if 'XMAS' is found, False otherwise
    """
    word = "XMAS"
    for k in range(len(word)):
        ni, nj = i + k * dr, j + k * dc
        if (
            not (0 <= ni < len(data) and 0 <= nj < len(data[0]))
            or data[ni][nj] != word[k]
        ):
            return False
    return True


def search_XMAS(data: List[List[str]]) -> int:
    """Search for all occurrences of the word 'XMAS' in the data.

    Args:
        data (List[List[str]]): The data to search in

    Returns:
        int: The number of occurrences of 'XMAS' in the data
    """
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # diagonal down-right
        (-1, 1),  # diagonal up-right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1),  # diagonal up-left
        (1, -1),  # diagonal down-left
    ]
    occurrences = 0

    # Iterate over the grid to search for 'XMAS' in all directions
    for i in range(len(data)):
        for j in range(len(data[i])):
            for dr, dc in directions:
                if check_XMAS(data, i, j, dr, dc):
                    occurrences += 1
    return occurrences


def main() -> None:
    # Read input data
    try:
        with open("in.txt") as f:
            raw_data = f.read()
    except FileNotFoundError:
        logging.error("Input file 'in.txt' not found.")
        return

    # Prepare data
    lines = raw_data.strip().split("\n")  # Split into lines
    data: List[List[str]] = [list(row) for row in lines]  # Convert to List[List[str]]

    # Search for XMAS in all directions
    total_occurrences = search_XMAS(data)

    print(f"Total occurrences of 'XMAS': {total_occurrences}")
    return None


if __name__ == "__main__":
    main()
