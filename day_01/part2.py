from collections import Counter


def main():
    left = []
    right = []
    score = 0

    with open("input.txt") as f:
        for line in f:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

    right_counts = Counter(right)

    for l in left:
        score += l * right_counts[l]
        print(score)


if __name__ == "__main__":
    main()
