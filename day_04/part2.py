import pathlib
import sys


def test_solve():
    test_input = pathlib.Path(__file__).parent / "test-input.txt"
    assert solve(test_input) == 9


def solve(input_file):
    data = []
    num_found = 0
    valid_pair = {"M", "S"}

    with open(input_file) as f:
        for line in f:
            data.append(line.strip())

    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - 1):
            if data[i][j] != "A":
                continue

            pair1 = {data[i - 1][j - 1], data[i + 1][j + 1]}
            pair2 = {data[i - 1][j + 1], data[i + 1][j - 1]}

            if pair1 == pair2 == valid_pair:
                num_found += 1

    return num_found


if __name__ == "__main__":
    fname = sys.argv[1]
    print(solve(fname))
