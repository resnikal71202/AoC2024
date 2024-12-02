"""Day 2 Part 1."""

from typing import Optional


class Report:
    """Report class."""

    def __init__(self, levels: str) -> None:
        """Init."""
        self.levels = list(map(int, filter(None, levels.split(" "))))

    def is_safe(self, levels: Optional[list[int]] = None) -> bool:
        """Check if the report is safe according to the rules.

        A report is safe if the levels are either all increasing or all decreasing,
        and any two adjacent levels differ by at least one and at most three.

        Args:
            levels (list[int], optional): The list of levels to check. If None,
                use self.levels.

        Returns:
            bool: True if the report is safe, False otherwise.
        """
        if levels is None:
            levels = self.levels

        if len(levels) < 2:
            # A report with fewer than 2 levels is considered safe
            return True

        # Calculate the differences between adjacent levels
        diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

        # Check if all differences are within the allowed range (1 to 3 inclusive)
        if not all(1 <= abs(d) <= 3 for d in diffs):
            return False

        # Determine the overall direction (increasing or decreasing)
        if all(d > 0 for d in diffs):
            return True
        elif all(d < 0 for d in diffs):
            return True
        else:
            return False


def main() -> None:
    """Find the number of save reports."""
    with open("in.txt") as f:
        reports = f.read()
    reports = reports.strip()
    print(sum([Report(rep).is_safe() for rep in reports.split("\n")]))
    return None


if __name__ == "__main__":
    main()
