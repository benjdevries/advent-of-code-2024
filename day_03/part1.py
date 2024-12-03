import re
import sys


def main():
    fname = sys.argv[1]
    instruction_match = re.compile(r"mul\((\d+),(\d+)\)")
    result = 0

    with open(fname) as f:
        for line in f:
            for match in instruction_match.finditer(line):
                x, y = match.groups()
                result += int(x) * int(y)

    print(result)


if __name__ == "__main__":
    main()
