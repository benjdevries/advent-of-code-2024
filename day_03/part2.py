import re
import sys


def main():
    fname = sys.argv[1]
    instruction_match = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")
    result = 0
    enabled = True

    with open(fname) as f:
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

    print(result)


if __name__ == "__main__":
    main()
