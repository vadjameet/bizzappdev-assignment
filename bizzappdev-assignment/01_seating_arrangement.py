"""
Problem: Seating Arrangement Problem
Approach: Model as a directed graph and check for Hamiltonian cycle.
Each guest must have exactly two neighbors. We verify if the graph forms a single cycle.
"""

def find_seating_arrangement(guests):
    from collections import defaultdict
    graph = defaultdict(list)
    for guest, prefs in guests.items():
        graph[guest] = prefs

    path = []
    visited = set()
    start = next(iter(guests.keys()))
    current = start
    while True:
        if current in visited:
            break
        visited.add(current)
        path.append(current)
        next_nodes = graph.get(current, [])
        if not next_nodes:
            return None
        current = next_nodes[0] if next_nodes[0] not in visited else next_nodes[1] if len(next_nodes) > 1 else None
        if current is None:
            return None

    if len(path) == len(guests) and path[-1] in graph.get(start, []):
        return path + [start]
    return None

# Example usage:
if __name__ == "__main__":
    guests = {
        'Alice': ['Bob', 'Carol'],
        'Bob': ['Alice', 'David'],
        'Carol': ['Alice', 'David'],
        'David': ['Bob', 'Carol']
    }
    arrangement = find_seating_arrangement(guests)
    if arrangement:
        print("Valid arrangement:", ' -> '.join(arrangement))
    else:
        print("No valid arrangement exists")