import pathlib
import sys


def test_solve():
    test_input = pathlib.Path(__file__).parent / "test-input.txt"
    assert solve(test_input) == 143


def is_valid_page(page: int, update: list[int], rules: tuple[int, int]):
    rule_pages_before = {r[0] for r in rules if r[1] == page}
    rule_pages_after = {r[1] for r in rules if r[0] == page}

    page_idx = update.index(page)
    actual_pages_before = set(update[:page_idx])
    actual_pages_after = set(update[page_idx + 1 :])

    return (
        actual_pages_before <= rule_pages_before
        and actual_pages_after <= rule_pages_after
    )


def solve(input_file):
    rules = []
    updates = []
    result = 0

    with open(input_file) as f:
        while (line := f.readline().strip()) != "":
            rules.append(tuple(int(x) for x in line.split("|")))

        for line in f:  # cursor is after the rules
            updates.append([int(x) for x in line.strip().split(",")])

    for update in updates:
        if all(is_valid_page(p, update, rules) for p in update):
            # Accumulate middle numbers
            result += update[len(update) // 2]

    return result


if __name__ == "__main__":
    fname = sys.argv[1]
    print(solve(fname))
