from myprofiler import profile

# the trade graph for smallest cost to get piano
graph = {}
graph["book"] = {"poster": 0, "lp": 5}
graph["poster"] = {"guitar": 30, "drums": 35}
graph["lp"] = {"guitar": 15, "drums": 20}
graph["guitar"] = {"piano": 20}
graph["drums"] = {"piano": 10}
graph["piano"] = {}

infinity = float("inf")

# the costs start form book
costs = {}
costs["poster"] = 0
costs["lp"] = 5
costs["guitar"] = infinity
costs["drums"] = infinity
costs["piano"] = infinity

# parents hash table for path
parents = {}
parents["poster"] = "book"
parents["lp"] = "book"
parents["guitar"] = None
parents["drums"] = None
parents["piano"] = None

# list of processed node
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
            lowest_cost = cost
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            parents[n] = node
            costs[n] = new_cost
    processed.append(node)
    node = find_lowest_cost_node(costs)


def dijkstra(start_node, end_node):
    path = []
    while end_node != start_node:
        path.append(end_node)
        end_node = parents[end_node]
    path.append(start_node)
    return path


print("The lowest costs from book to piano is: ", end="\n\n")
for i in dijkstra("book", "piano"):
    print(i, end=" ")
print()
