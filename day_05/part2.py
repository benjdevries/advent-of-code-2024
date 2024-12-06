import collections
import sys

# def test_solve():
#     test_input = pathlib.Path(__file__).parent / "test-input.txt"
#     assert solve(test_input) == 143


def dfs(graph, start, seen=None, path=None):
    if seen is None:
        seen = []
    if path is None:
        path = [start]

    seen.append(start)
    paths = []

    for node in graph[start]:
        if node not in seen:
            node_path = path + [node]
            paths.append(tuple(node_path))
            paths.extend(dfs(graph, node, seen[:], node_path))

    return paths


def solve(input_file):
    page_graph = collections.defaultdict(list)
    updates = []
    result = 0

    with open(input_file) as f:
        while (line := f.readline().strip()) != "":
            start, end = (int(x) for x in line.split("|"))
            page_graph[start].append(end)

        for line in f:  # cursor is after the rules
            updates.append([int(x) for x in line.strip().split(",")])

    print(len(page_graph))

    for edges in page_graph.values():
        print(len(edges))

    # for update in updates:
    #     paths = dfs(page_graph, update[0])
    #     if all(set(p) != set(update) for p in paths):
    #         print(f"No valid path for {update}")

    return result


if __name__ == "__main__":
    fname = sys.argv[1]
    print(solve(fname))
