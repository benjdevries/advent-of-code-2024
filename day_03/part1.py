import pathlib
import re
import sys


def test_solve():
    test_input = pathlib.Path(__file__).parent / "test-input-1.txt"
    assert solve(test_input) == 161


def solve(input_file):
    instruction_match = re.compile(r"mul\((\d+),(\d+)\)")
    result = 0

    with open(input_file) as f:
        for line in f:
            for match in instruction_match.finditer(line):
                x, y = match.groups()
                result += int(x) * int(y)

    return result


if __name__ == "__main__":
    fname = sys.argv[1]
    print(solve(fname))
