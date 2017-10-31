import random
import time

class DVertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = []

    def getID (self):
        return self.id

    def addNeighbor(self,nbr):
        self.connectedTo = self.connectedTo + [nbr]

    def getConnections(self):
        return self.connectedTo

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = []

    def addNeighbor(self, nbr):
        self.connectedTo = self.connectedTo + [nbr]

    def getConnections(self):
        return self.connectedTo

    def getID(self):
        return self.id


#Some Global Constants Used
source = open("facebook_combined.txt", "r")
Total_Edges = sum(1 for line in source)
data_set = [0] * Total_Edges
undirected_set = [0] * Total_Edges
source.close()
sub_data_set = []

## generate_graph () generates an entire adjacency list.
def generate_graph ():
    # Change source
    source = open("facebook_combined.txt", "r")
    # Create a list with certain length
    for i in source.readlines():
        ID = ""
        Adjacent = ""
        pos = 0
        while i[pos] != " ":
            ID = ID + i[pos]
            pos = pos + 1

        while i[pos] == " ":
            pos = pos + 1
        while i[pos] != " ":
            Adjacent = Adjacent + i[pos]
            pos = pos + 1
        ID = int(ID)
        Adjacent = int (Adjacent)

        ## Generate a set of directed Vertices
        if data_set[ID] == 0:
            data_set[ID] = DVertex(ID)
            DVertex.addNeighbor(data_set[ID], Adjacent)
        else:
            DVertex.addNeighbor(data_set[ID], Adjacent)

        ## Generate a set of undirected Vertices
        if undirected_set[ID] == 0:
            undirected_set[ID] = Vertex(ID)
            Vertex.addNeighbor(undirected_set[ID], Adjacent)
        else:
            Vertex.addNeighbor(undirected_set[ID], Adjacent)

        if undirected_set[Adjacent] == 0:
            undirected_set[Adjacent] = Vertex(ID)
            Vertex.addNeighbor(undirected_set[Adjacent], ID)
        else:
            Vertex.addNeighbor(undirected_set[Adjacent], ID)

        ID = ""
        Adjacent = ""

    source.close()

generate_graph()
# for i in data_set:
#     if i == 0:
#         continue
#     else:
#         print DVertex.getConnections(i)

# for i in undirected_set:
#     if i == 0:
#         continue
#     else:
#         print Vertex.getConnections(i)
#undirected/ directed set look like  [Vertix, Vertix, 0, Vertix......]
# We can use Total_Edges


#print undirected_set
#def motif_sampling (n, trials):
#     total = trials
#     generate_graph(n)  # Generates a data set
#     while (trials != 0):
#         print str(total - trials) + ": "
#         single_motif_sampling(n, trials)
#         trials = trials - 1
#

inside = []
## select_first_edge() allows us to randomly select one edge
## from the graph we generated
## Void -> Void
## Effect: prints the "inside Vertex" list
##         Modifies the inside Vertex
## Requires generated data_se.
def select_first_edge ():
    r = random.randint(1, Total_Edges)
    sum = 0
    for i in range (0, Total_Edges - 1):
        if data_set[i] == 0:
            continue
        elif sum + len (DVertex.getConnections(data_set[i])) >= r:
            # use sum - r - 1 to get the index
            V1 = DVertex.getConnections(data_set[i])[sum + len (DVertex.getConnections(data_set[i])) - r - 1]
            V2 = DVertex.getID(data_set[i])
            inside = [V1, V2]
            print inside
            break
        else:
            sum = sum + len (DVertex.getConnections(data_set[i]))

select_first_edge()


#     undirected_set_copy = undirected_set
#     Vertex.getConnections(undirected_set_copy[V1]).remove(V2)
#     Vertex.getConnections(undirected_set_copy[V2]).remove(V1)
#     ## If both sets are empty, then call the sampling function again.
#     if len(DVertex.getConnections(data_set[V1])) == 0 and len(DVertex.getConnections(data_set[V1])) == 0:
#         motif_sampling (n, trials)
#     sub_data_set = [undirected_set_copy[V1], undirected_set_copy[V2]]
#
#     sampling(n - 1, sub_data_set, undirected_set_copy)
#
# def sampling (n, sub_data_set, undirected_set_copy):
#
#     sub_edges = 0
#     for i in sub_data_set:
#         if i == 0:
#             continue
#         else:
#             sub_edges = sub_edges + len(Vertex.getConnections(i))
#     while n > 1:
#         sum = 0
#         sub_edges = 0
#         for i in sub_data_set:
#             if i == 0:
#                 continue
#             else:
#                 sub_edges = sub_edges + len (Vertex.getConnections(i))
#         if sub_edges < n:
#             break
#         r = random.randint (0, sub_edges)
#         for i in sub_data_set:
#             if i == 0:
#                 continue
#             elif len(Vertex.getConnections(i)) + sum >= r:
#                 # Add the new Vertix to the sub_data_set.
#                 sub_data_set = sub_data_set + [undirected_set_copy[Vertex.getConnections(i)[sum + len(Vertex.getConnections(i)) - r - 1]]]
#                 print "(" + str (Vertex.getConnections(i)[sum + len(Vertex.getConnections(i)) - r - 1]) \
#                       + " , " + str(Vertex.getID(i)) + ")"
#                 Vertex.getConnections(i).remove(Vertex.getConnections(i)[sum + len(Vertex.getConnections(i)) - r - 1])
#                 break
#             else:
#                 sum = sum + len(Vertex.getConnections(i))
#         n = n - 1
#
# motif_sampling(5, 1000)