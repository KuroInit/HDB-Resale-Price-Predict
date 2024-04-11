from heapq import heappush, heappop


def greedy_best_first_search(startState, heuristicFunc):
    global goalNode, maxFringeSize, maxDepthReached
    visited, pQueue = set(), list()

    # For GBFS, the priority is determined only by the heuristic function.
    key = heuristicFunc(startState)
    root = State(startState, None, None, 0, 0, key)
    entry = (
        key,
        0,
        root,
    )  # Note: The second element is kept for consistency with your A* format.
    heappush(pQueue, entry)

    while pQueue:
        node = heappop(pQueue)
        visited.add(node[2].map)

        if node[2].state == goalState:
            goalNode = node[2]
            return True  # The goal has been reached.

        neighbors = expand(node[2])
        for neighbor in neighbors:
            # The node's key is the heuristic value since we're not considering the cost so far.
            neighbor.key = heuristicFunc(neighbor.state)
            entry = (
                neighbor.key,
                neighbor.move,
                neighbor,
            )  # The second element is the move count.

            # If it's not visited, or if it's a more efficient path, add to the queue.
            if neighbor.map not in visited:
                heappush(pQueue, entry)
                visited.add(neighbor.map)

                # Update the maximum depth reached if necessary.
                maxDepthReached = max(maxDepthReached, neighbor.depth)

        # Update the maximum fringe size if necessary.
        maxFringeSize = max(maxFringeSize, len(pQueue))

    return False  # If the queue is empty and the goal wasn't reached, return False.
