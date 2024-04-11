from queue import Queue

def brute_force_search(start_state):
    global maxDepthReached, maxFringeSize, goalNode
    
    # Define the goal state for an 8-puzzle.
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    # Create a queue for BFS and add the initial state.
    frontier = Queue()
    root = State(start_state, None, None, 0, 0, 0)
    frontier.put(root)
    
    # Set for keeping track of visited states.
    explored = set()
    explored.add(root.map)
    
    # Loop until all states are explored or the goal is found.
    while not frontier.empty():
        # Remove the state at the front of the queue.
        current_state = frontier.get()
        
        # Check if this state is the goal state.
        if current_state.state == goal_state:
            goalNode = current_state
            return True
        
        # Generate all possible child states.
        children = expand(current_state)
        
        # Add the new states to the frontier if they haven't been explored.
        for child in children:
            if child.map not in explored:
                frontier.put(child)
                explored.add(child.map)
                maxDepthReached = max(maxDepthReached, child.depth)
        
        # Keep track of the maximum size of the frontier.
        maxFringeSize = max(maxFringeSize, frontier.qsize())
    
    # Return False if no solution was found.
    return False