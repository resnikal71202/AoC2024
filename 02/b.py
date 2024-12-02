"""Day 2 Part 2."""

import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


class Report:
    """Report class representing a single report of levels."""

    def __init__(self, levels_str: str) -> None:
        """Initialize the Report with levels parsed from a string.

        Args:
            levels_str (str): A string containing levels separated by spaces.
        """
        # Parse the levels from the input string into a list of integers
        self.levels = list(map(int, filter(None, levels_str.strip().split())))
        # Initialize the number of dampeners available (1 per report)
        self.dampeners = 1
        logging.debug(
            f"Initialized Report with levels: {self.levels}",
            " and dampeners: {self.dampeners}",
        )

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
            logging.debug("Report is safe (fewer than 2 levels)")
            return True

        # Calculate the differences between adjacent levels
        diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
        logging.debug(f"Differences between levels: {diffs}")

        # Check if all differences are within the allowed range (1 to 3 inclusive)
        if not all(1 <= abs(d) <= 3 for d in diffs):
            logging.debug("Report is unsafe (difference out of allowed range)")
            return False

        # Determine the overall direction (increasing or decreasing)
        if all(d > 0 for d in diffs):
            return True
        elif all(d < 0 for d in diffs):
            return True
        else:
            return False

    def is_safe_with_dampener(self) -> bool:
        """Check if the report is safe, considering the Problem Dampener.

        The Problem Dampener allows the removal of a single level to make
        an unsafe report safe.

        Returns:
            bool: True if the report is safe or can be made safe by removing one level,
                False otherwise.
        """
        # First, check if the report is already safe without using the dampener
        if self.is_safe(self.levels):
            return True

        # Try removing each level one at a time to see if the report becomes safe
        for i in range(len(self.levels)):
            if self.dampeners <= 0:
                # No dampeners left to use
                logging.debug("No dampeners left to use")
                break

            # Create a new list of levels without the i-th level
            modified_levels = self.levels[:i] + self.levels[i + 1 :]
            logging.debug(
                f"Trying report without level at index {i}: {modified_levels}"
            )

            # Check if the modified report is safe
            if self.is_safe(modified_levels):
                logging.debug(f"Report is safe after removing level at index {i}")
                return True  # The report can be made safe by removing one level

        logging.debug("Report cannot be made safe even after using dampener")
        return False


def main() -> None:
    """Process the input reports and count the number of safe reports."""
    with open("in.txt") as f:
        reports_data = f.read()
    reports_data = reports_data.strip()
    report_lines = [line for line in reports_data.split("\n") if line.strip()]

    safe_reports_count = 0

    for rep in report_lines:
        report = Report(rep)
        if report.is_safe_with_dampener():
            safe_reports_count += 1

    print(safe_reports_count)


if __name__ == "__main__":
    main()
