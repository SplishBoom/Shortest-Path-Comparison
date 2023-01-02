from heapq import heappush, heappop

class AStar:
    """
    Pseduo Code of A* Algorithm:
    1. Initialize a priority queue Q and a distances array D.
    2. Insert the starting vertex into Q and set its distance in D to 0.
    3. While Q is not empty:
        4. Extract the vertex v with the minimum distance + heuristic cost from Q.
        5. For each neighbor w of v:
            6. Calculate the distance from the starting vertex to w through v.
            7. If this distance is less than the current distance in D for w, update the distance in D for w.
            8. Calculate the heuristic cost from w to the end vertex.
            9. If w is not in Q, add it to Q with a priority equal to the distance + heuristic cost.
    10. The distances array D now contains the shortest distances from the starting vertex to all other vertices.
    11. By backtracking from the end vertex, we can find the shortest path.
    12. Return the shortest path and its cost.
    """

    def __init__(self) -> None:
        """
        Constructor of AStar class.
        """
        self.iterations = {
            
        }

    def _a_star(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that takes an dictionary which includes a directed and weighted graph. Than it finds the shortest path by using A* algorithm. With heuristic function of abs(i-j)
        @params:
            graph -> dict : dictionary which includes a directed and weighted graph in the format {node: {neighbour: weight, neighbour: weight, ...}, ...}.
            start -> int : start node.
            end -> int : end node.
        @returns:
            algorithm_type -> str : name of the algorithm.
            path -> list : list of nodes, that are in the shortest path in order.
            cost -> int : cost of the shortest path.
            distance -> int : distance of the shortest path.
        """

        heuristic = lambda i, j: min(abs(i-j), abs(i-j))
        # Manhattan distance -> abs(i-j)
        # Euclidean distance -> (i-j)**2
        # Chebyshev distance -> max(abs(i-j), abs(i-j))
        # Minkowski distance -> (abs(i-j)**p)**(1/p)
        # Diagonal distance  -> min(abs(i-j), abs(i-j))
        # Dijkstra           -> 0

        # Initialize a priority queue Q and a distances array D.
        Q = []
        D = {}

        # Insert the starting vertex into Q and set its distance in D to 0.
        heappush(Q, (0, start))
        D[start] = 0

        # While Q is not empty:
        while Q:
            # Extract the vertex v with the minimum distance + heuristic cost from Q.
            _, v = heappop(Q)

            # For each neighbor w of v:
            for w in graph[v]:
                # Calculate the distance from the starting vertex to w through v.
                d = D[v] + graph[v][w]

                # If this distance is less than the current distance in D for w, update the distance in D for w.
                if w not in D or d < D[w]:
                    D[w] = d

                    # Calculate the heuristic cost from w to the end vertex.
                    h = heuristic(w, end)

                    # If w is not in Q, add it to Q with a priority equal to the distance + heuristic cost.
                    heappush(Q, (d+h, w))

        # Get the distance from the D array mapping.
        distance = D[end]

        # The distances array D now contains the shortest distances from the starting vertex to all other vertices.
        # By backtracking from the end vertex, we can find the shortest path.
        path = []
        cost = D[end]
        while end != start:
            for v in graph:
                if end in graph[v] and D[end] == D[v] + graph[v][end]:
                    path.append(end)
                    end = v
                    break
        path.append(start)
        path.reverse()

        # Return values.
        return (
            "AStar", 
            path, 
            cost, 
            distance
        )

    def solve(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that runs the A* algorithm. @_a_star().
        @params:
            graph -> dict : dictionary which includes a directed and weighted graph in the format {node: {neighbour: weight, neighbour: weight, ...}, ...}.
            start -> int : start node.
            end -> int : end node.
        @returns:
            algorithm_type -> str : name of the algorithm.
            path -> list : list of nodes, that are in the shortest path in order.
            cost -> int : cost of the shortest path.
            distance -> int : distance of the shortest path.
        """
        return self._a_star(graph, start, end)