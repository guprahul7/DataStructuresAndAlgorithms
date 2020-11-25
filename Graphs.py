
#=================== GRAPHS =======================

#Graphs are a more general structure than trees, we can think of a tree as a special kind of graph
#GRaphs can be used to represent many real-world things such as systems of roads, airline flights from city to city, how the internet is connected, etc

#VERTEX - (aka node) 
    #This is the fundamental part of a graph
    #It can have a name - (key)
    #May have additional info - (payload)

#EDGE - connects two nodes (to show there is rel'ship b/w them)
    #Edges may be one-way or two-wayu
    #If the edges in a graph are all one-way, we say that the graph is a directed graph, or a digraph
    
#WEIGHT
    #Edges may be weighted to show that there is a cost to go from one vertex to another
    #Example: In a graph of roads that connect one city to another, the weight on the edge might represent the distance between the two cities


#-------- Formal Definition of a GRAPH ---------

#A graph can be represented by G where G = (V, E)
    #V is a set of vertices - E is a set of edges

#Each edge is a tuple (v,w) where w,v -> V  #w,v belongs to V
#We can add a third component to the edge tuple to represent a WEIGHT
#A subgraph 's' is a set of ( edges 'e' and vertices 'v' ) such that e is subset of E and v is subset of V

#Example of Graph:
    # V = {V0, V1, V2, V3,  V4, V5}     These are vertices (or nodes)

    # E = { 
    #       (v0,v1,5), (v1,v2,4), (v2,v3,9), (v3,v4,7), (v4,v0,1),
    #       (v0,v5,2), (v5,v4,8), (v3,v5,3), (v5,v2,1)
    #      }    #These are edges showing relationship between the nodes/vertices


#--------- PATH ----------
#A path in a graph is a sequence of vertices that are connected by edges
#Formal definition: -> w_1, w_2,...,w_n  such that (w_i, w_i+1) -> E for all 1 <= i <= n-1
#The unweighted path length is the number of edges in the path, specifically n-1
#The weighted path length is the sum of the weights of all the edges in the path

#Example of path from V3 to V1 (from above graph):
    #The sequence of vertices: (V3, V4, V0, V1)
    #The edges are { (v3,v4,7), (v4,v0,1), (v0,v1,5) }


#---------- CYCLE ----------
#A cycle in a directed graph is a path that starts and ends at the same vertex
#A graph with no cycles is called an acyclic graph
#A directed graph with no cycles is called a Directed-Acyclic-Graph or DAG
#Several important problems can be solved if it can be represented as a DAG 
#Cycle - starting and ending at same node



#================ IMPLEMENTING A GRAPH ================


# -------- Adjacency Matrix Implementation -------

# One of the easiest ways to implement a graph - 2D matrix
# Each row an column represent a vertex in the graph
# The value stored in the cell at the intersection of row v and column w indicates if there is an edge from vertex v to vertex w
# When two vertices are connected by an edge, we say that they are adjacent

# Adv of adjacency matrix is that it is simple, and for small graphs it ie easy to see which noedes are connected to other nodes
# Most of the cells in the matrix are empty
# Because most of the cells are empty, we say that the matrix is 'sparse'
# A matrix is not a very efficient way to store sparse data
# Adj Matrix is good for a graph when the number of edges is large
# Since there is 1row and 1col for every vertex in the graph, the number of edges required to fill the matrix is |V|^2
#A matrix is full when every vertex is connected to every other vertex




# -------- Adjacency List Implementation -------

# A more space-efficient way to implement a sparsely connected graph is to use an adjacency list
# In an adj-list we keep a master list of all the vertices in the Graph object and then each vertex object in the graph maintains a list of the other vertices that it is connected to.
# In our implementation of the Vertex class we will use a dictionary rather than a list, where the dictionary keys are the vertices, and the values are the weights
#Adv of adj-list is that it allows us to compactly represent a sparse graph
#The adjacency list also allows us to easily find all the links that re directly connected to a particular vortex

#Implementation - Create two classes:
    #Graph: which hold the master list of vertices
    #Vertex: which will represent reach vertex in the graph

#Vertex Class:
#Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the weight of each edge
    #This dictionary is called 'connectedTo. The constructor simply initializes the id, (which is typically a string), and the connectedTo dictionary
    #The addNeighbor method is used to add a connection from this vertex to another
    #The getConnections method returns all of the vertices in the adjacency-list, as represented by the connectedTo instance variable
    #The getWeight method returns the weight of the edge from this vertex to the vertex passed as a parameter

class Vertex(object):

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight     #adding connection to Vertex, by putting the new connection info in the dictionary, key=neighbor, value=weight

    def getConnections(self):
        return self.connectedTo.keys()      #Getting all connections of the Vertex 

    def getId(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __str__(self):      #Special method, the string method, this is what happens when python needs a string representation, 
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])           #Basically when you say print the Vertex object, python will look for the string representation  


#Graph Class:
#In order to implement a graph as an adj-list, what we need to do is define the methods our adj-list object will have:
    #Graph() - creates a new, empty graph
    #addVertex(vert) - adds an isntance of Vertex to the graph
    #addEdge(fromVert, toVert) - adds a new, directed edge to the graph that connects the two vertices
    #getVertex(vertKey) - finds the vertex in the graph named vertKey
    #getVertices() - returns the list of all vertices in the graph
    #in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, otherwise False

class Graph(object):

    def __init__(self): 
        self.vertList = {}      #list of all vertices in a graph
        self.numVertices = 0    #number of vertices

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:     #since vertlist is a dictionary, the 'in' check default refers to keys
            return self.vertList[n]
        else:
            return None
        
    def addEdge(self, fromVertex, toVertex, weight=0):
        if fromVertex not in self.vertList:
            nv = self.addVertex(fromVertex)
        if toVertex not in self.vertList:
            self.addVertex(toVertex)

        self.vertList[fromVertex].addNeighbor(self.vertList[toVertex], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):             #special method __iter__ in case we want to iterate through the graph object
        return iter(self.vertList.values()) #will make it possible to iterate through the values in the vertList, which are actually the vertices/Vertex-objects in the graph

    def __contains__(self,n):       #checking if graph contains a vertex n
        return n in self.vertList     #returns True or False


g = Graph()         #create new instance of graph

for i in range(6):  #add 6 vertices to that graph
    g.addVertex(i)

print(g.vertList)   #checking the list of vertices in the graph
print('\n')

g.addEdge(0,1,2)    #adding edge/connection from one vertex to another
#g.addEdge(fromVertex=0, toVertex=1, weight=2)   

for vertex in g:    #iterating through g graph (possible because we created an iterable function to in the graph class to make this possible)
    print (vertex)
    print (vertex.getConnections())
    print ('\n')




#=============== WORD LADDER PROBLEM =================

#Example: turn 'FOOL' into 'SAGE' by changing each letter at a time, but you cannot have an invalid word during the changes  

#Approach:
    #Represent the relationships between the words as a graph
    #Use the graph algorithm known as BFS to find an efficient path from the starting word to the ending word

    #Figure out how to turn a large collection of words into a graph
    #We would like to have an edge from one word to another if the two words are only different by a single letter
    #Then any path from one word to another is a solution to the word ladder puzzle



#=============== BREADTH FIRST SEARCH ================




#=========== Implementation of Graph Overview =========

#OrderedDict - just like a normal dictionary, except it remembers the order in which the items are inserted into it
from enum import Enum 
from collections import OrderedDict

class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3

class Node:
    
    def __init__(self, num):
        self.num = num          #ID of the node
        self.visit_state = State.unvisited  #
        self.adjacent = OrderedDict()   #to keep track of who all it is connected to #key = node, value = weight

    def __str__(self):          #when you call print fn, it will invoke this fn. 
        return str(self.num)    #will return number of the node

class Graph:
    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self,num):
        node = Node(num)
        self.nodes[num] = node  
        return node    

    def add_edge(self, Fnode, Tnode, weight=0):
        if Fnode not in self.nodes:
            self.add_node(Fnode)
        if Tnode not in self.nodes:
            self.add_node(Tnode)
    
        self.nodes[Fnode].adjacent[self.nodes[Tnode]] = weight

g = Graph()
g.add_edge(0,1,5)
print(g.nodes)
g.add_edge(1,2,3)


# ========= IMPLEMENTATION OF DEPTH FIRST SEARCH (basis stack) ===========
graph = {
         'A': set(['B','C']),
         'B': set(['A','D','E']),
         'C': set(['A','F']),
         'D': set(['B']),
         'E': set(['B','F']),
         'F': set(['C','E']), 
         }

def DFS(graph, start):
    visited = set()     #keep track of visited nodes so that you don't visit again
    stack = [start] 

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
        
        stack.extend(graph[vertex]-visited)


# ----------- Implementation of BFS (basis queue) ------------ 
def BFS(graph, start):  #shortest path algorithm
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)

        return visited
            


