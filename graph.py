graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "pegg"]
graph["alice"] = ["pegg"]
graph["claire"] = ["tom", "jonny"]
graph["pegg"] = []
graph["tom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person): # pseudocodigo
            print(person + " is a mango seller")
            return True
        else:
            search_queue += graph(person)
            searched.append(person)

    return False

search("you")