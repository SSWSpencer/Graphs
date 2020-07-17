"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        ##pass  # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
       # pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
           self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #pass  # TODO

        #create an empty queue
        q = []
        #create a set for visited nodes
        visited = []

        #init: enqueue the starting node
        q.append(starting_vertex)
        # while the queue is not empty,
            # dequeue first item
            #if it's not been visited
                #mark as vistied (add to the visited set)
                # add all neighbors to the queue

        while len(q) > 0:
            v = q[0]
            q.pop(0)
            
            if v not in visited:
                visited.append(v)
                print(v)
                for next_vert in self.get_neighbors(v):
                    q.append(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #pass  # TODO
        s = []
        visited = set()
        s.append(starting_vertex)
        while len(s) > 0:
            v = s[0]
            s.pop(0)

            if v not in visited:
                visited.add(v)
                print(v)
                for next_vert in self.get_neighbors(v):
                    s.insert(0, next_vert)

    def dft_recursive(self, starting_vertex, visited=None, path=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #pass  # TODO
        # Mark all the vertices as not visited 
        s = []
        visited = set()
        s.append(starting_vertex)
        while len(s) > 0:
            v = s[0]
            s.pop(0)

            if v not in visited:
                visited.add(v)
                print(v)
                for next_vert in self.get_neighbors(v):
                    s.insert(0, next_vert)
        


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #pass  # TODO
        path = []
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            last_vert = path[-1]
            
            if last_vert not in visited:
                if last_vert == destination_vertex:
                    return path

                else:
                    visited.add(last_vert)

                for neighbor in self.get_neighbors(last_vert):
                    copypath = path.copy()
                    copypath.append(neighbor)
                    q.enqueue(copypath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #pass  # TODO
        path = []
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path = s.pop()
            last_vert = path[-1]
            
            if last_vert not in visited:
                if last_vert == destination_vertex:
                    return path

                else:
                    visited.add(last_vert)

                for neighbor in self.get_neighbors(last_vert):
                    copypath = path.copy()
                    copypath.append(neighbor)
                    s.push(copypath)

    

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #pass  # TODO
        if visited is None:
            visited =  set()

        if path is None:
            path = []
            path.append(starting_vertex)

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            if path[-1] == destination_vertex:
                return path
            for next_vertex in self.get_neighbors(starting_vertex):
                cpath = list(path)
                cpath.append(next_vertex)
                rpath = self.dfs_recursive(next_vertex, destination_vertex, visited, cpath)
                if rpath is not None:
                    return rpath


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(f"vertices: {graph.vertices}")

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("bft:")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft")
    graph.dft(1)
    print("dft recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("dfs")
    print(graph.dfs(1, 6))
    print("recursive dfs")
    print(graph.dfs_recursive(1, 6))
