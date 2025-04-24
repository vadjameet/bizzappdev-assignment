"""
Problem: Shortest Path Finder using Dijkstra's Algorithm
Approach: Priority queue implementation of Dijkstra's algorithm.
"""
import heapq

def dijkstra(cities, start, end):
    distances = {city: float('inf') for city in cities}
    distances[start] = 0
    prev = {}
    heap = [(0, start)]
    
    while heap:
        current_dist, current = heapq.heappop(heap)
        if current == end:
            break
        for neighbor, weight in cities[current].items():
            if (new_dist := current_dist + weight) < distances[neighbor]:
                distances[neighbor] = new_dist
                prev[neighbor] = current
                heapq.heappush(heap, (new_dist, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current in prev:
        path.append(current)
        current = prev[current]
    path.append(start)
    return path[::-1], distances.get(end, -1)

# Example usage:
if __name__ == "__main__":
    cities = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'C': 3, 'D': 9},
        'C': {'A': 10, 'B': 3, 'D': 1},
        'D': {'B': 9, 'C': 1}
    }
    path, distance = dijkstra(cities, 'A', 'D')
    print(f"Shortest path: {' -> '.join(path)}")
    print(f"Total distance: {distance}")