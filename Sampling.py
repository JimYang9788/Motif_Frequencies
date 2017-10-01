import random

# Some Global Constants Used
source_file = open("facebook_combined.txt", "r")
Total_Edges = sum(1 for line in source_file)

# data_set is an adjacency list that stores a directed graph
data_set = [[]] * Total_Edges

# undirected_set is an adjacency list that stores a undirected graph
undirected_set = [[]] * Total_Edges

source_file.close()


# generate_graph (data) generates an entire adjacency list.
# It takes in the name of the txt file from the same directory
# and produce an adjacency list, stored in data_set and
# undirected_set.

def generate_graph(data):
    input_file = open(data, "r")
    for i in input_file.readlines():
        vertex_id = ""
        vertex_adjacent = ""
        pos = 0
        while i[pos] != " ":
            vertex_id = vertex_id + i[pos]
            pos = pos + 1

        while i[pos] == " ":
            pos = pos + 1
        while i[pos] != " ":
            vertex_adjacent = vertex_adjacent + i[pos]
            pos = pos + 1
        vertex_id = int(vertex_id)
        vertex_adjacent = int(vertex_adjacent)

        # Generate a set of directed Vertices
        data_set[vertex_id] = data_set[vertex_id] + [vertex_adjacent]

        # Generate a set of undirected Vertices
        undirected_set[vertex_id] = undirected_set[vertex_id] + [vertex_adjacent]
        undirected_set[vertex_adjacent] = undirected_set[vertex_adjacent] + [vertex_id]

        vertex_id = ""
        vertex_adjacent = ""

    input_file.close()


# select_first_edge() allows us to randomly select one edge
# from the graph we generated
# Void -> Void
# Effect: prints the "inside Vertex" list
#         Modifies the inside Vertex
# Requires generated data_se.
def select_first_edge():
    r = random.randint(1, Total_Edges)
    acc_edges = 0
    for i in range(Total_Edges):
        if acc_edges + len(data_set[i]) >= r:
            # use sum - r - 1 to get the index
            v1 = data_set[i][r - acc_edges - 1]
            v2 = i
            selected = [v1, v2]
            return selected
        else:
            acc_edges = acc_edges + len(data_set[i])


# sampling (size) takes in the size of motif we need
# to sample, then prints the chosen motifs.

def sampling(size):
    inside = select_first_edge()  # All the vertices inside of our selection
    cur_vertices = 2  # Current number of vertices in the inside array

    v1 = inside[0]  # First vertex
    v2 = inside[1]  # Second vertex

    neighbours_1 = undirected_set[v1]
    neighbours_2 = undirected_set[v2]
    neighbours = [neighbours_1, neighbours_2]

    outside_edges = [len(neighbours_1) - 1, len(neighbours_2) - 1]

    # This will be the random number that we use later.
    total_outsiders = outside_edges[0] + outside_edges[1]

    while size - 1 != 0:

        # edge_acc is an accumulator that used to select random generated edge.
        edge_acc = 0
        r = random.randint(1, total_outsiders)
        # r is a randomly generated number between 1 and all outsiders
        for i in range(cur_vertices):

            if edge_acc + outside_edges[i] >= r:
                pick = r - edge_acc   # We pick the pick-th element in the neighbour[i] that is not an insider
                index = 0

                while pick != 0:
                    if index == len(neighbours[i]) - 1:
                         break
                    if (neighbours[i])[index] not in inside:
                        pick = pick - 1
                        index = index + 1
                    else:
                        index = index + 1

                new_vertex = (neighbours[i])[index - 1]
                inside = inside + [new_vertex]

                new_neighbour = undirected_set[new_vertex]

                # connected keeps track of all new outsiders coming from the new_vertex
                new_outsider = 0
                for i in new_neighbour:
                    if i in inside:
                        continue
                    else:
                        new_outsider = new_outsider + 1

                outside_edges = outside_edges + [len(new_neighbour)]

                total_outsiders = total_outsiders + new_outsider

                cur_vertices = cur_vertices + 1

                for i in range(cur_vertices - 1):
                    if new_vertex in neighbours[i]:
                        outside_edges[i] = outside_edges[i] - 1

                neighbours = neighbours + [new_neighbour]
                break

            else:
                edge_acc = edge_acc + outside_edges[i]
        size = size - 1
    print inside


# motif_sampling is the main function.
def motif_sampling(size, trials, data):
    generate_graph(data)
    for i in range(trials):
        sampling(size)


motif_sampling(6, 1000, "facebook_combined.txt")
