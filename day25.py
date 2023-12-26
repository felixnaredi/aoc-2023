# %% First Star
# ------------------------------------------------------------------------------

graph = {}
for line in input.splitlines():
    parent, children = line.split(":")
    for child in children[1:].split(" "):
        # NOTE:
        #   Fill in the important edges after hand here. I used graphviz neato to
        #   identify the edges.
        #
        if ( False
        #     (parent == "abc" and child == "def")
        #     or (parent == "def" and child == "abc")
        #     or (parent == "ghi" and child == "jkl")
        #     or (parent == "jkl" and child == "ghi")
        #     or (parent == "mno" and child == "prq")
        #     or (parent == "prq" and child == "mno")
        ):
            pass
        else:
            if graph.get(parent):
                graph[parent].append(child)
            else:
                graph[parent] = [child] 
            if graph.get(child):
                graph[child].append(parent)
            else:
                graph[child] = [parent] 

#
# NOTE:
#   Generate graphviz file. The following command will generate an jpeg that can
#   be used to identify the edges:
#   ```
#   neato -Tjpg temp.dot > temp.jpg
#   ```
#
with open("temp.dot", "w") as file:
    print("graph {", file=file)
    for node, children in graph.items():
        for child in children:
            print(f"{node} -- {child}", file=file)
    print("}", file=file)

visited = [set(), set()]
for i, root in enumerate(("htm", "zvl")):
    queue = [(0, root)]
    distances = {}
    while len(queue) != 0:
        dist, node = queue.pop(0)
        if node not in visited[i]:
            visited[i].add(node)
            distances[node] = dist
            for child in graph[node]:
                queue.append((dist + 1, child))

print(len(visited[0]) * len(visited[1]))


# %% Second Star
# ------------------------------------------------------------------------------

