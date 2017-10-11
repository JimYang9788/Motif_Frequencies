import random
from sets import Set

# The 0th item is data_set[0], {1,2,3,4,5,6,7}
# data_set = [{1,2,3,4,5,6,7,8},{48,53...}.....]
vertices = []
source_file = open("facebook_combined.txt", "r")

for i in source_file.readlines():
    if (i.split())[0] not in vertices:
        vertices = vertices + [(i.split())[0]]
    elif (i.split())[1] not in vertices:
        vertices = vertices + [(i.split())[1]]

total_vertices = len(vertices)
source_file.close()

data_set = [set() for i in range(total_vertices)]  # Create a data_set with size equal to the number of vertices

total_edges = 0
size_set = []  # size set is an array of number of neighbours that each vertex has

def generate_graph():
    source_file = open("facebook_combined.txt", "r")

    for i in source_file.readlines():
        current_edge = i.split()
        (data_set[int((current_edge[0]))]).add(int(current_edge[1]))
        (data_set[int((current_edge[1]))]).add(int(current_edge[0]))
    source_file.close

    return total_edges

generate_graph()




def sampling_first_pair ():
    chosen_vertices = []
    chosen_edges = []
    neighbour_list = []
    data_array = []
    size_set = []
    total_edges = 0

    for j in data_set:
        data_array = data_array + [list(j)]

    for k in range(total_vertices):
        size_set = size_set + [len(data_set[k])]

    for l in size_set:
        total_edges = total_edges + l

    r = random.randint (1, total_edges)

    acc = 0
    for i in range(total_vertices):
        if acc + size_set[i] < r:
            acc = size_set[i] + acc
        else:
            i_th_element = r - acc - 1
            extended_vertex = (data_array[i])[i_th_element]
            chosen_edges.append([i, extended_vertex])

            # Temporarily remove the two vertex from the data_set
            # Create a new neighbour list from the data_set

            data_set[i].remove(extended_vertex)
            data_set[extended_vertex].remove(i)
            neighbour_list.append (data_set[i])
            neighbour_list.append(data_set[extended_vertex])
            chosen_vertices.append(i)
            chosen_vertices.append(extended_vertex)
            break
    return [chosen_vertices, chosen_edges, neighbour_list]

def sampling_rest (n, chosen_vertices, chosen_edges, neighbour_list):
    ## print neighbour_list
    while n > 0:
        data_array = []
        size_array = []
        total_neighbours = 0
        acc = 0

        for i in neighbour_list:
            data_array = [list(i)] + data_array
            size_array = [len(i)] + size_array
            total_neighbours = len(i) + total_neighbours

        if total_neighbours <= n:
            break   # When the Vertex does not contain more than 1 neighbour
        r = random.randint(1, total_neighbours)

        for i in range(len(neighbour_list)):
            if acc + size_array[i] < r:
                acc = acc + size_array[i]
            else:
                i_th_element = r - acc - 1
                extended_vertex = data_array[i][i_th_element]
                # print chosen_vertices
                # print i
                # #print neighbour_list
                # print len (neighbour_list)
                chosen_edges.append([chosen_vertices[i], extended_vertex])
                chosen_vertices.append(extended_vertex)
                break
        for i in chosen_vertices:
            for j in chosen_vertices:
                if j in data_set[i]:
                    data_set[i].remove(j)
        n = n - 1
    # print chosen_edges
    # print chosen_vertices



def motif_sampling (n, trial_times):
    sampling_first_pair()
    for k in range(trial_times):
        result = sampling_first_pair()
        chosen_vertices = result[0]
        chosen_edges = result[1]
        neighbour_list = result [2]
        sampling_rest(n - 1, chosen_vertices, chosen_edges, neighbour_list)
        for j in chosen_edges:
            data_set[j[0]].add(j[1])
            data_set[j[1]].add(j[0])



motif_sampling(7, 5000)
