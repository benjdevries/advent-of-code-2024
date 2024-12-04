import pathlib
import re
import sys


def test_solve():
    test_input = pathlib.Path(__file__).parent / "test-input-2.txt"
    assert solve(test_input) == 48


def solve(input_file):
    instruction_match = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")
    result = 0
    enabled = True

    with open(input_file) as f:
        for line in f:
            for instruction in instruction_match.finditer(line):
                match instruction.group():
                    case "do()":
                        enabled = True
                    case "don't()":
                        enabled = False
                    case _ if enabled:
                        x, y = instruction.groups()
                        result += int(x) * int(y)

    return result


if __name__ == "__main__":
    fname = sys.argv[1]
    print(solve(fname))
