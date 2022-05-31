"""
Problem Statement:
Given an integer n representing the number of courses (courses are labeled from 0 to n-1), and an array of prerequisites
where prerequisites[i] = [a, b] means that you first need to take course b before taking course a, determine if it's
possible to finish all the courses
"""
from collections import deque

"""
Initial Thoughts:
Another search algorithm... breadth first search? (BFS)
Would want to arrange directed graph in dependency order
    Topological sort, but not possible if there is a cycle
If you find dependency cycle can immediately return false
Hamiltonian Path??????
"""
"""
Video Thoughts:
Want to find a dependency cycle to prove its false, otherwise true.
Strongly recommend using a graph to at least visualize the problem
In a linked list (ordered/directed graph), keep track of each node visited and if visited twice, then there is a 
    dependency
DFS if coded incorrectly will not return correct results
Topological sort will help with DFS though
    Finding a linear ordering of vertices such that each vertex comes after its prerequisites
    Cannot work when there is a cycle
        Use this to advantage for this problem
    pick a vertex, and put it on a path stack
        Once you find a vertex with no neighbors unvisited, pop vertex and put it on order stack, 
        then continue down the list and keep popping and pushing from path stack to order stack
"""
def dfs(graph, vertex, path, order, visited):
    # Pushing current vertex onto path stack
    path.add(vertex)
    # Loop running through dependencies from this vertex to the end
    for neighbor in graph[vertex]:
        # Before moving to new neighbor, check if its already in stack
        if neighbor in path:
            return False
        if neighbor not in visited:
            # The smaller problem is finding out if a vertex has any unvisited neighbors, can start popping from path
            # stack and pushing onto order stack when smallest problem is found
            visited.add(neighbor)
            # This is checking to see if we have already found a cycle, that it continues up the chain
            if not dfs(graph, neighbor, path, order, visited):
                return False
    # Saves ordering of path pushes so when it comes back it pushes classes w/ dependencies first
    path.remove(vertex)
    order.append(vertex)
    return True
def top_sort(graph):
    visited = set()
    path = []
    order = []
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(graph, vertex, path, order, visited)
    return order[::-1]
def course_schedule(n, prerequisites):
    graph = [[] for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(prep[0])
        visited = set()
        path = set()
        order = []
        for course in range(n):
            if course not in visited:
                if not dfs(graph, course, path, order, visited):
                    return False
    return True
"""
Can also use Breadth First Search:
Do this by split directed graph into levels:
    first level is no prereqs, then remove that level
    continue process until at end of levels
COding wise, need to update list every time you remove a level,
    remove in-degrees (how many edges it has pointing towards it)
    Put 0 in-degree vertices in queue first, then when popped and pushed into order remove 1 in-degree from 
    corresponding vertices that used previous vertex as an edge
"""
def bfs_course_schedule(n, prerequisities):
    # declaring graph and prerequisite variables
    graph = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    # initializing graph and indegrees using given information
    for pre in prerequisities:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    order = []
    # Placing classes with no prereqs on queue first
    queue = deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            # Decrementing neighbors in-degrees since current vertex has been removed from stack so no longer there
            indegree[neighbor] -= 1
            # Only adds from path to queue once its confirmed there are no prereqs left (unvisited neighbors)
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    # Setting n equal to length of order; if there is a cycle BFS won't have all the classes and would return False
    return len(order) == n

if __name__ == '__main__':
    print("temp")
