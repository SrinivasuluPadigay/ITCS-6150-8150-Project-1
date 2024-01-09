import heapq

class Node:
    def __init__(self, state, goal_state, parent=None, g_cost=0):
        """
        Initialize a Node object for the 8-puzzle problem.
        Args:
        state (list): The current state of the puzzle represented as a list.
        goal_state (list): The goal state of the puzzle represented as a list.
        parent (Node, optional): The parent node in the search tree. Defaults to None.
        g_cost (int, optional): The cost from the start node to the current node. Defaults to 0.
        """
        self.state = state      # The current state of the puzzle
        self.parent = parent    # The parent node in the search tree
        self.g_cost = g_cost    # g-cost represents the cost from the start node to the current node
        self.h_cost = self.calculate_h_cost(goal_state)  # h-cost represents the heuristic cost
        self.f_cost = self.g_cost + self.h_cost  # f-cost is the sum of g-cost and h-cost

    def calculate_h_cost(self, goal_state):
        """
        Calculate the number of misplaced tiles between the current state and the goal state.
        Returns:
        int: The number of misplaced tiles.
        """
        misplaced_count = 0

        for i in range(9):
            if self.state[i] != goal_state[i]:
                misplaced_count += 1

        return misplaced_count

    def __lt__(self, other):
        # Compare nodes based on their f-cost
        return self.f_cost < other.f_cost

def a_search(case_input, case_goal):
    open_nodes = []          # Priority queue for open nodes
    explored_nodes = set()   # Set to store explored states
    initial_node = Node(case_input, case_goal)
    heapq.heappush(open_nodes, initial_node)     # Add the initial node to the open list
    nodes_generated = 1     # Count of nodes generated (initialized to 1 for the initial node)
    nodes_expanded = 0      # Count of nodes expanded

    while open_nodes:
        current_node = heapq.heappop(open_nodes)  # Get the node with the lowest f(n) value
        current_state = current_node.state
        nodes_expanded += 1

        if current_state == case_goal:     # Check if the goal state is reached
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1], nodes_generated, nodes_expanded

        explored_nodes.add(tuple(current_state))  # Add the current state to the closed set

        empty_tile_index = current_state.index(0)
        row, col = divmod(empty_tile_index, 3)
        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in possible_moves:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = current_state[:]
                new_empty_tile_index = new_row * 3 + new_col
                new_state[empty_tile_index], new_state[new_empty_tile_index] = new_state[new_empty_tile_index], new_state[empty_tile_index]
                g_cost = current_node.g_cost + 1
                child_node = Node(new_state, case_goal, parent=current_node, g_cost=g_cost)
                nodes_generated += 1

                if tuple(new_state) not in explored_nodes:      # Check if the new state is not in the closed set
                    heapq.heappush(open_nodes, child_node)   # Add the child node to the open list

    return None, nodes_generated, nodes_expanded    # Return None if no solution is found

def process(case_input, case_goal):
    path, nodes_generated, nodes_expanded = a_search(case_input, case_goal)

    if path:
        print("Solution found!")
        for step, state in enumerate(path):
            print(f"Step {step}:")
            for i in range(0, 9, 3):
                print(state[i:i + 3])
            print()
        print(f"Nodes generated: {nodes_generated}")
        print(f"Nodes expanded: {nodes_expanded}")
        print()
    else:
        print("No solution found.")
