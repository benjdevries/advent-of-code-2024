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


def is_dampended_report_safe(report: list[int]):
    for i in range(len(report)):
        dampened_report = report[:]
        dampened_report.pop(i)
        if is_report_safe(dampened_report):
            return True
    return False


def main():
    num_safe = 0

    with open("input.txt") as f:
        for report in f:
            report = [int(x) for x in report.split()]
            if is_dampended_report_safe(report):
                num_safe += 1

    print(num_safe)


if __name__ == "__main__":
    main()
