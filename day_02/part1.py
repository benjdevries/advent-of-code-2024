import pathlib
import sys


def test_solve():
    test_input = pathlib.Path(__file__).parent / "test-input.txt"
    assert solve(test_input) == 2


def is_report_safe(report: list[int]) -> bool:
    """Whether a given reactor report is safe

    Reports are safe when values are either all increasing
    or all decreasing and each subsequent value differs by
    1, 2, or 3

    Args:
        report (list[int]): List of ints representing report

    Returns:
        bool: True if report is safe, false if not
    """
    diffs = [j - i for i, j in zip(report[:-1], report[1:], strict=False)]
    return all(-3 <= x <= -1 for x in diffs) or all(1 <= x <= 3 for x in diffs)


def solve(input_file):
    num_safe = 0

    with open(input_file) as f:
        for report in f:
            report = [int(x) for x in report.split()]
            if is_report_safe(report):
                num_safe += 1

    return num_safe


if __name__ == "__main__":
    fname = sys.argv[1]
    print(solve(fname))
