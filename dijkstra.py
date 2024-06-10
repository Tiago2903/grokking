graph = {}
graph["a"] = {}
graph["b"] = {}
graph["start"] = {}

graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"]["fin"] = 6
graph["b"]["a"]["fin"] = 2
graph["b"]["fin"] = 2

graph["fin"] = {}

print(graph["start"].keys())