import re
import sys


def main():
    fname = sys.argv[1]
    data = []
    num_found = 0

    with open(fname) as f:
        for line in f:
            data.append(line.strip())

    # Horizontal
    vectors = [*data]

    # Vertical
    for chars in zip(*data, strict=True):
        vectors.append("".join(chars))

    # NW-SE Diagonal
    for j in range(len(data) - 1, -1, -1):
        diag = []
        for i in range(len(data)):
            j += 1
            if j > len(data):
                break
            diag.append(data[i][j - 1])
        if len(diag) >= 4:
            vectors.append("".join(diag))

    for i in range(len(data) - 1):
        diag = []
        for j in range(len(data)):
            i += 1
            if i > len(data) - 1:
                break
            diag.append(data[i][j])
        if len(diag) >= 4:
            vectors.append("".join(diag))

    # NE-SW Diagonal
    for j in range(len(data) + 1):
        diag = []
        for i in range(len(data)):
            j -= 1
            if j < 0:
                break
            diag.append(data[i][j])
        if len(diag) >= 4:
            vectors.append("".join(diag))

    for i in range(1, len(data)):
        diag = []
        for j in range(len(data) - 1, -1, -1):
            i += 1
            if i > len(data):
                break
            diag.append(data[i - 1][j])
        if len(diag) >= 4:
            vectors.append("".join(diag))

    num_found = 0
    xmas_matcher = re.compile(r"(?=XMAS|SAMX)")
    for v in vectors:
        matches = xmas_matcher.findall(v)
        num_found += len(matches)

    print(num_found)


if __name__ == "__main__":
    main()
