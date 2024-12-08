import logging
from collections import defaultdict, deque

logging.basicConfig(level=logging.INFO)


class Rule:
    """Represents a single ordering rule."""

    def __init__(self, rule: str) -> None:
        """Initialize rule with left and right page numbers."""
        self.left, self.right = map(int, rule.split("|"))

    def __str__(self) -> str:
        return f"{self.left} | {self.right}"

    def __repr__(self) -> str:
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


def reorder_update(update: list[int], rules: list[Rule]) -> list[int]:
    """Reorder the update using topological sorting based on the rules."""
    # Build a graph and in-degree count for topological sorting
    graph = defaultdict(set)
    in_degree: defaultdict[int, int] = defaultdict(int)

    for rule in rules:
        if rule.left in update and rule.right in update:
            graph[rule.left].add(rule.right)
            in_degree[rule.right] += 1

    # Include all nodes in the graph with zero in-degree
    for page in update:
        if page not in in_degree:
            in_degree[page] = 0

    # Perform topological sort
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages


def main() -> None:
    """Main function to process updates and calculate the result."""
    rules, updates = parse_input("in.txt")

    # Separate valid and invalid updates
    invalid_updates = [
        update for update in updates if not is_update_valid(update, rules)
    ]
    reordered_updates = [reorder_update(update, rules) for update in invalid_updates]

    # Compute the sum of middle pages for reordered updates
    middle_sum = sum(get_middle_page(update) for update in reordered_updates)
    logging.info(f"The sum of the middle pages of reordered updates is: {middle_sum}")


if __name__ == "__main__":
    main()
