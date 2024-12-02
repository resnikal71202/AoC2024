"""Day 2 Part 1."""


class Report:
    """Report class."""

    def __init__(self, levels: str) -> None:
        """Init."""
        self.levels = list(map(int, filter(None, levels.split(" "))))

    def check_diff(self, diff: int, dir: int) -> bool:
        """Check if the difference is valid.

        Args:
            diff (int): difference between two levels.
            dir (int): direction of the levels.

        Returns:
            bool: True if the difference is valid, False otherwise.
        """
        if dir > 0 and (diff > 3 or diff <= 0):
            return False
        if dir < 0 and (diff < -3 or diff >= 0):
            return False
        return True

    def is_safe(self) -> bool:
        """check if the Report is save.
        The report is save if the level decreases or increases by not more than 3.

        Returns:
            bool: True if the report is save, False otherwise.
        """
        dir = self.levels[1] - self.levels[0]
        if dir == 0:
            return False
        for i in range(len(self.levels) - 1):
            diff = self.levels[i + 1] - self.levels[i]
            if not self.check_diff(diff, dir):
                return False
        return True


def main() -> None:
    """Find the number of save reports."""
    with open("in.txt") as f:
        reports = f.read()
    reports = reports.strip()
    print(sum([Report(rep).is_safe() for rep in reports.split("\n")]))
    return None


if __name__ == "__main__":
    main()
