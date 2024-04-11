def greedy_best_first_search(start_state, goal_state):
    global maxFringeSize, goalNode
    
    # Create a priority queue for GBFS and add the initial state with a priority based on the heuristic value.
    frontier = PriorityQueue()
    root = State(start_state, None, None, 0, heuristic(start_state, goal_state), 0)
    frontier.put((root.heuristic, root))
    
    # Set for keeping track of visited states.
    explored = set()
    explored.add(root.map)
    
    # Loop until all states are explored or the goal is found.
    while not frontier.empty():
        # Remove the state with the lowest heuristic value (highest priority) from the queue.
        _, current_state = frontier.get()
        
        # Check if this state is the goal state.
        if current_state.state == goal_state:
            goalNode = current_state
            return True
        
        # Generate all possible child states.
        children = expand(current_state)
        
        # Add new states to the frontier if they haven't been explored or if they have a lower heuristic value.
        for child in children:
            if child.map not in explored:
                child.heuristic = heuristic(child.state, goal_state)
                frontier.put((child.heuristic, child))
                explored.add(child.map)
                # No need to track maxDepthReached since GBFS does not expand the deepest node first.
        
        # Keep track of the maximum size of the frontier.
        maxFringeSize = max(maxFringeSize, frontier.qsize())
    
    # Return False if no solution was found.
    return False
