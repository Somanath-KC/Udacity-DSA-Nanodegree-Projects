from math import sqrt
import heapq as hq


class PriorityQueue:
    def __init__(self, items=[]):
        self.arr = items[:]
        hq.heapify(self.arr)

    def put(self, value):
        hq.heappush(self.arr, value)

    def get(self):
        return hq.heappop(self.arr)

    def isempty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)


class GraphNode:
    def __init__(self, value=None, weight=None):
        self.value = value
        self.weight = weight

    def __lt__(self, node):
        return self.weight < node.weight

    def __repr__(self):
        return str(self.value) + ": " + str(self.weight)


def calc_distance(start, stop):
    """
        Heuristic Distance

        Euclidean formula to calculate distance
        between 2 data points in a plane.
        It is calculated using the Minkowski Distance formula
        by setting ‘p’ value to 2, thus, also known as the
        L2 norm distance metric. It is usually used in calculating
        diagnol distance.

        Formula: sqrt((x1 - x2)**2 + (y1 - y2)**2)

        Other than Eucliden formula we can also use
        Manhattan Distance formula to calculate distance
        in the vector space or grid directions. This is usually
        used for finding path on roads(grid based) & non-diagnol paths.

        Formula: abs(x2-x1) + abs(y2-y1)

        Below is the implementation of Manhattan Distance formula.

        Ref: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

    """
    x1, y1 = start
    x2, y2 = stop
    return abs(x2-x1) + abs(y2-y1)


def get_path(prev, start, goal):
    # print(prev)
    current = goal
    path = [current]
    while current != start:
        current = prev[current]
        path += [current]
    return path[::-1]


def shortest_path(graph, start, goal):

    intersecs = graph.intersections
    roads = graph.roads

    paths = PriorityQueue()
    paths.put(GraphNode(start, 0))

    origin, cost = {start: None}, {start: 0}

    while paths.size() > 0:
        current_node = paths.get().value
        # print(paths)  # Used for debugging

        if current_node == goal:
            get_path(origin, start, goal)

        if current_node not in origin:
            origin[current_node] = 0

        if current_node not in cost:
            cost[current_node] = 0

        for node in roads[current_node]:
            c_inter = intersecs[current_node]
            n_inter = intersecs[node]
            c_to_n_distance = calc_distance(c_inter, n_inter)
            new_distance = cost[current_node] + c_to_n_distance

            if node not in cost or new_distance < cost[node]:
                cost[node] = new_distance
                totalScore = new_distance + \
                    calc_distance(intersecs.get(current_node, (0, 0)),
                                  intersecs.get(node, (0, 0)))
                paths.put(GraphNode(node, totalScore))
                origin[node] = current_node
            else:
                # print(cost, paths)  # Used for Debugging
                pass
    return get_path(origin, start, goal)

# Ref: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# Ref: https://knowledge.udacity.com/questions/384146
# Ref: https://knowledge.udacity.com/questions/195897
