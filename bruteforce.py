from heapq import heappush, heappop

def greedy_best_first_search(startState, heuristicFunc):
    global goalNode, maxFringeSize, maxDepthReached
    visited, pQueue = set(), list()
    
    # The key for GBFS is the heuristic value alone.
    key = heuristicFunc(startState)
    root = State(startState, None, None, 0, key)
    entry = (key, root)
    heappush(pQueue, entry)
    
    while pQueue:
        current_key, currentNode = heappop(pQueue)
        visited.add(currentNode.map)
        
        # Check if the current node is the goal.
        if currentNode.state == goalState:
            goalNode = currentNode
            return True
        
        # Generate neighbors (successors)
        neighbors = expand(currentNode)
        for neighbor in neighbors:
            # For GBFS, the priority is the heuristic value only.
            neighbor.key = heuristicFunc(neighbor.state)
            entry = (neighbor.key, neighbor)
            if neighbor.map not in visited:
                heappush(pQueue, entry)
                visited.add(neighbor.map)
                maxDepthReached = max(maxDepthReached, neighbor.depth)
        
        # Track the maximum size of the priority queue.
        maxFringeSize = max(maxFringeSize, len(pQueue))
    
    # If the function exits the loop, no solution was found
    return False

# Example usage:
# Define the heuristic function (e.g., Manhattan distance for 8-puzzle)
def heuristicFunc(state):
    # Implement the heuristic function here
    pass

# Define the State class and expand function as per your problem specification
# Define the goal state accordingly
goalState = [1, 2, 3, 4, 5, 6