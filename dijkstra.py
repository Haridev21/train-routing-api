import heapq

TRAIN_CHANGE_PENALTY = 20   # distance penalty for changing trains

def dijkstra(graph, source, destination):
    distances = {}
    for station in graph:
        distances[station] = float("inf")
    distances[source] = 0

    parent = {}
    train_used = {}

    # Priority queue: (distance, station, last_train)
    pq = [(0, source, None)]

    while pq:
        current_dist, current_station, last_train = heapq.heappop(pq)

        if current_dist > distances[current_station]:
            continue

        if current_station == destination:
            break

        for edge in graph.get(current_station, []):
            next_station = edge["to"]
            weight = edge["weight"]
            train_no = edge["train"]

            new_dist = current_dist + weight

            # Apply penalty if train changes
            if last_train is not None and train_no != last_train:
                new_dist += TRAIN_CHANGE_PENALTY

            if new_dist < distances.get(next_station, float("inf")):
                distances[next_station] = new_dist
                parent[next_station] = current_station
                train_used[next_station] = train_no
                heapq.heappush(pq, (new_dist, next_station, train_no))

    # Reconstruct path
    path = []
    curr = destination

    while curr in parent or curr == source:
        path.append({
            "station": curr,
            "train": train_used.get(curr)
        })
        if curr == source:
            break
        curr = parent[curr]

    path.reverse()

    return {
        "source": source,
        "destination": destination,
        "total_distance": distances[destination],
        "path": path
    }
