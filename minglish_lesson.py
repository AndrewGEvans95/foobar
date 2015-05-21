def createGraph(words):
    graph = {}
    rows = len(words)
    for row in range(rows - 1):
        edge = find_edge(words[row], words[row + 1])

        if edge is not None:
            node, direction = edge
            if node in graph:
                graph[node].append(direction)
            else:
                graph[node] = [direction]
    return graph


def find_edge(a, b):
    length = min(len(a), len(b))
    for c in range(length):
        if a[c] != b[c]:
            return a[c], b[c]


def start_nodes(graph):
    tmp = set()
    for edges in graph.values():
        for edge in edges:
            tmp.add(edge)
    secondtmp = set()
    for node in graph:
        if node not in tmp:
            secondtmp.add(node)
    return secondtmp

def answer(words):
    graph = createGraph(words)
    start = start_nodes(graph)
    letters = []
    traversed = []
    def visit(node):
        if node not in traversed:
            traversed.append(node)

            if node in graph:
                for edge in graph[node]:
                    visit(edge)
            letters.append(node)

    for node in start:
        visit(node)
    return ''.join(letters[::-1])