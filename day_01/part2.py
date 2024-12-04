import pathlib
import sys
from collections import Counter


def test_solve():
    test_input = pathlib.Path(__file__).parent / "test-input.txt"
    assert solve(test_input) == 31


def solve(input_file):
    left = []
    right = []
    score = 0

    with open(input_file) as f:
        for line in f:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

    right_counts = Counter(right)

    for l in left:
        score += l * right_counts[l]

    return score


if __name__ == "__main__":
    fname = sys.argv[1]
    print(solve(fname))
