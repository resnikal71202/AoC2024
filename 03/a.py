# Day 3 part 1

import logging
import re

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """Day 3 Part 1."""
    with open("in.txt") as f:
        data = f.read()
    data = data.strip()

    # write a regex to match the string mul(X,Y) where x and y are integers
    # with a maximum of 3 digits
    reg = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    # find all matches
    matches = reg.findall(data)
    logging.debug(matches)

    # multiply the two numbers and sum them
    result = sum([int(x) * int(y) for x, y in matches])
    logging.info(result)

    return None


if __name__ == "__main__":
    main()
