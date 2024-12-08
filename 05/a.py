import logging

logging.basicConfig(level=logging.INFO)


class Rule:
    """Represents a single ordering rule."""

    def __init__(self, rule: str) -> None:
        """Initialize rule with left and right page numbers."""
        self.left, self.right = map(int, rule.split("|"))

    def __str__(self) -> str:
        """Return the string representation of the rule."""
        return f"{self.left} | {self.right}"

    def __repr__(self) -> str:
        """Return the string representation of the rule."""
        return self.__str__()

    def is_valid(self, pages: list[int]) -> bool:
        """Check if the rule is respected in the given page order."""
        if self.left in pages and self.right in pages:
            return pages.index(self.left) < pages.index(self.right)
        return True  # Rule is irrelevant if one or both pages are missing.


def parse_input(file_path: str) -> tuple[list[Rule], list[list[int]]]:
    """Parse input from the file and return rules and updates."""
    with open(file_path) as f:
        data = f.read().strip()
    rules_section, updates_section = data.split("\n\n")
    rules = [Rule(rule) for rule in rules_section.splitlines()]
    updates = [
        list(map(int, update.split(","))) for update in updates_section.splitlines()
    ]
    return rules, updates


def is_update_valid(update: list[int], rules: list[Rule]) -> bool:
    """Check if the update respects all applicable rules."""
    return all(rule.is_valid(update) for rule in rules)


def get_middle_page(update: list[int]) -> int:
    """Return the middle page number of the update."""
    return update[len(update) // 2]


def main() -> None:
    """Main function to process updates and calculate the result."""
    rules, updates = parse_input("in.txt")
    valid_updates = [update for update in updates if is_update_valid(update, rules)]
    middle_sum = sum(get_middle_page(update) for update in valid_updates)
    logging.info(f"The sum of the middle pages of valid updates is: {middle_sum}")
    return None


if __name__ == "__main__":
    main()
