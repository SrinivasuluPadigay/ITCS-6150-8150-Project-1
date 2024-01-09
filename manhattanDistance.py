from queue import PriorityQueue

class Node:
    def __init__(self, state=None, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue
        x_goal, y_goal = divmod(goal.index(state[i]), 3)
        x_cur, y_cur = divmod(i, 3)
        distance += abs(x_cur - x_goal) + abs(y_cur - y_goal)
    return distance

def get_neighbors(node):
    neighbors = []
    x, y = divmod(node.state.index(0), 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = node.state[:]
            new_state[x * 3 + y], new_state[nx * 3 + ny] = new_state[nx * 3 + ny], new_state[x * 3 + y]
            neighbors.append(Node(state=new_state, parent=node, cost=node.cost + 1, heuristic=0))
    return neighbors

def a_star_search(initial_state, goal):
    open_queue = PriorityQueue()
    open_set = {}
    explored = set()

    initial_node = Node(state=initial_state, parent=None, cost=0, heuristic=manhattan_distance(initial_state, goal))
    open_queue.put(initial_node)
    open_set[tuple(initial_state)] = initial_node.total_cost

    nodes_generated = 1
    nodes_explored = 0

    while not open_queue.empty():
        current_node = open_queue.get()

        if tuple(current_node.state) in explored:
            continue

        nodes_explored += 1
        explored.add(tuple(current_node.state))

        if current_node.state == goal:
            path = []
            while current_node:
                path.insert(0, current_node.state)
                current_node = current_node.parent
            return path, nodes_generated, nodes_explored

        for neighbor in get_neighbors(current_node):
            neighbor_tuple = tuple(neighbor.state)
            neighbor.heuristic = manhattan_distance(neighbor.state, goal)
            neighbor.total_cost = neighbor.cost + neighbor.heuristic

            if neighbor_tuple in explored:
                continue

            if neighbor_tuple not in open_set or open_set[neighbor_tuple] > neighbor.total_cost:
                open_queue.put(neighbor)
                open_set[neighbor_tuple] = neighbor.total_cost
                nodes_generated += 1

    # Return None if no solution is found
    return None, nodes_generated, nodes_explored

def process(case_input, case_goal):
    path, nodes_generated, nodes_expanded = a_star_search(case_input, case_goal)

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