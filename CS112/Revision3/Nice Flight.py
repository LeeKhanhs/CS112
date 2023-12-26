import heapq

def dijkstra(adj_list, source):
    # Number of cities
    n = len(adj_list) - 1
    inf = float('inf')

    # Initialize distances with infinity for all cities
    distances = [inf] * (n + 1)
    distances[source] = 0

    # Priority queue to store (distance, city) tuples
    pq = [(0, source)]

    # Dijkstra's algorithm
    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Skip if already found a shorter path
        if current_dist > distances[current_node]:
            continue

        # Update distances for neighboring cities
        for neighbor, weight in adj_list[current_node]:
            distance = current_dist + weight

            # Relaxation step
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def main():
    # Input: Number of cities, Number of flights
    n, m = map(int, input().split())

    # Adjacency list for flights in forward and reverse directions
    adj_list = [[] for _ in range(n + 1)]
    adj_list_reverse = [[] for _ in range(n + 1)]

    # List to store flight details
    edge_list = []

    # Input: Flight details
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_list[u].append((v, w))
        adj_list_reverse[v].append((u, w))
        edge_list.append((u, v, w))

    # Calculate distances using Dijkstra's algorithm in both directions
    distance_forward = dijkstra(adj_list, 1)
    distance_reverse = dijkstra(adj_list_reverse, n)

    # Find the minimum cost considering the voucher discount
    ans = float('inf')
    for u, v, w in edge_list:
        ans = min(ans, distance_forward[u] + w // 2 + distance_reverse[v])

    # Output: Minimum cost
    print(ans)

if __name__ == "__main__":
    main()