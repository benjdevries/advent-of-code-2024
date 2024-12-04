import pathlib
import sys


def test_solve():
    test_input = pathlib.Path(__file__).parent / "test-input.txt"
    assert solve(test_input) == 11


def solve(input_file):
    left = []
    right = []
    diff = 0

    with open(input_file) as f:
        for line in f:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

    left.sort()
    right.sort()

    for l, r in zip(left, right, strict=False):
        diff += abs(l - r)

    return diff


if __name__ == "__main__":
    fname = sys.argv[1]
    print(solve(fname))
