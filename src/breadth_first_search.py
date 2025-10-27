from collections import deque
from collections.abc import Callable
from pathlib import Path
from utils.json_reader import JSONReader

# Performance: O(V+E)

class BreadthFirstSearch:
    """Breadth First algorithm."""
    
    @staticmethod
    def search(name: str, graph: dict, condition: Callable[..., bool]) -> bool:
        """Search."""
        search_queue: deque = deque()
        search_queue += graph[name]
        searched: set = set()

        while search_queue:
            person: str = search_queue.popleft()
            if person not in searched:
                if condition(person):
                    print(person + " is a mango seller!")
                    return True
                else:
                    search_queue += graph[person]
                    searched.add(person)
        return False
    


def person_is_seller(person: str) -> bool:
    return person[-1] == 'm'

graph: dict[str, list[str]] = JSONReader.read_json(path=Path("assets/bfs_graph.json"))
BreadthFirstSearch.search(
    name="you",
    graph=graph,
    condition=person_is_seller
)