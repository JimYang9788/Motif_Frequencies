import random
import copy
from sets import Set

# The 0th item is adjacency_list[0], {1,2,3,4,5,6,7}
# adjacency_list = [{1,2,3,4,5,6,7,8},{48,53...}.....]
vertices = []
source_file = open("facebook_combined.txt", "r")

for i in source_file.readlines():
    if (i.split())[0] not in vertices:
        vertices = vertices + [(i.split())[0]]
    elif (i.split())[1] not in vertices:
        vertices = vertices + [(i.split())[1]]

total_vertices = len(vertices)
source_file.close()

adjacency_list = [set() for i in range(total_vertices)]
# Create a adjacency_list with size equal to the number of vertices

total_edges = 0

copy_adjacency_list = [set() for i in range(total_vertices)]


def generate_graph():
    source_file = open("facebook_combined.txt", "r")

    for i in source_file.readlines():
        current_edge = i.split()
        (adjacency_list[int((current_edge[0]))]).add(int(current_edge[1]))
        (adjacency_list[int((current_edge[1]))]).add(int(current_edge[0]))
    source_file.close()

    source_file = open("facebook_combined.txt", "r")
    for i in source_file.readlines():
        current_edge = i.split()
        (copy_adjacency_list[int((current_edge[0]))]).add(int(current_edge[1]))
        (copy_adjacency_list[int((current_edge[1]))]).add(int(current_edge[0]))


    source_file.close
    return total_edges

def sampling_first_pair ():
    chosen_vertices = []
    chosen_edges = []
    neighbour_list = []
    neighbour_array = []
    size_set = []  # size set is an array of number of neighbours that each vertex has
    total_edges = 0

    for j in adjacency_list:
        neighbour_array = neighbour_array + [list(j)]
        size_set = size_set + [len(j)]
        total_edges = total_edges + len(j)

    r = random.randint (1, total_edges)

    acc = 0
    for i in range(total_vertices):
        if acc + size_set[i] < r:
            acc = size_set[i] + acc
        else:
            i_th_element = r - acc - 1
            extended_vertex = (neighbour_array[i])[i_th_element]

            # Temporarily remove the two vertex from the adjacency_list
            # Create a new neighbour list from the adjacency_list

            adjacency_list[i].remove(extended_vertex)
            adjacency_list[extended_vertex].remove(i)

            neighbour_list.append (adjacency_list[i])
            neighbour_list.append(adjacency_list[extended_vertex])

            chosen_vertices.append(i)
            chosen_vertices.append(extended_vertex)

            chosen_edges.append([i, extended_vertex])
            break
    return [chosen_vertices, chosen_edges, neighbour_list]

def sampling_rest (n, chosen_vertices, chosen_edges, neighbour_list, add_back_list):

    while n > 0:
        neighbour_array = []
        size_array = []
        total_neighbours = 0
        acc = 0

        for i in neighbour_list:
            neighbour_array = [list(i)] + neighbour_array
            size_array = [len(i)] + size_array
            total_neighbours = len(i) + total_neighbours

        if total_neighbours < 1:
            break   # When the Vertex does not contain more than 1 neighbour
        r = random.randint(1, total_neighbours)

        for i in range(len(neighbour_list)):
            if acc + size_array[i] < r:
                acc = acc + size_array[i]
            else:
                i_th_element = r - acc - 1
                extended_vertex = neighbour_array[i][i_th_element]

                # Update Chosen Edges
                chosen_edges.append([chosen_vertices[i], extended_vertex])

                # Update Chosen Vertices
                chosen_vertices.append(extended_vertex)

                # Update the Adjacency List
                for i in chosen_vertices:
                    for j in chosen_vertices:
                        if j in adjacency_list[i]:
                            adjacency_list[i].remove(j)
                            add_back_list.append([i, j])

                # Update Neighbour list
                neighbour_list = []
                for i in chosen_vertices:
                    neighbour_list = [list (adjacency_list[i])] + neighbour_list
                break

        n = n - 1


def motif_sampling (n, trial_times):
    generate_graph()

    for k in range(trial_times):
        result = sampling_first_pair()
        chosen_vertices = result[0]
        chosen_edges = result[1]
        neighbour_list = result [2]
        add_back_list = [(result[1])[0]]
        sampling_rest(n - 1, chosen_vertices, chosen_edges, neighbour_list, add_back_list)

        #
        # print chosen_vertices
        # print add_back_list

        for j in add_back_list:
            adjacency_list[j[0]].add(j[1])
            adjacency_list[j[1]].add(j[0])

        size_five(chosen_vertices)


def size_three (chosen_vertices):
    num_list = [0,0,0]
    if chosen_vertices[0] in adjacency_list[(chosen_vertices[1])]:
        num_list[0] = num_list[0] + 1
    if chosen_vertices[0] in adjacency_list[(chosen_vertices[2])]:
        num_list[0] = num_list[0] + 1

    if chosen_vertices[1] in adjacency_list[(chosen_vertices[0])]:
        num_list[1] = num_list[1] + 1
    if chosen_vertices[1] in adjacency_list[(chosen_vertices[2])]:
        num_list[1] = num_list[1] + 1

    if chosen_vertices[2] in adjacency_list[(chosen_vertices[0])]:
        num_list[2] = num_list[2] + 1
    if chosen_vertices[2] in adjacency_list[(chosen_vertices[1])]:
        num_list[2] = num_list[2] + 1

    num_list.sort()
    size_code = "".join([str(num) for num in num_list])
    if size_code == "112":
        print "type1"
    elif size_code == "222":
        print "type2"
    else:
        print "Something went wrong"

def size_five (chosen_vertices):
    num_list = [[],[],[],[],[]]
    neighbour_number = [0,0,0,0,0]
    unique_code = ["" for i in range(5)]
    result_list = [[],[],[],[],[]]

    for i in range(5):
        for j in range(5):
            if chosen_vertices[i] in copy_adjacency_list[chosen_vertices[j]]:
                num_list[i] = num_list[i] + [j]
                neighbour_number[i] = neighbour_number[i] + 1

    for i in range(5):
        for j in range(len(num_list[i])):
            result_list[i] = result_list[i] + [neighbour_number[(num_list[i][j])]]
        result_list[i].sort(reverse=True)

    for i in range(5):
        unique_code[i] = "".join(str(j) for j in result_list[i])

    unique_code.sort()
    unique_code.sort(key = len, reverse=True)
    unique_code = "".join(unique_code)
    num_list.sort(reverse=True)
    neighbour_number.sort(reverse=True)

    if unique_code == "11114444":
        print "type1"
    elif unique_code == "21131233":
        print "type2"
    elif unique_code == "2211424244":
        print "type3"
    elif unique_code == "21212222":
        print "type4"
    elif unique_code == "3213213333":
        print "type5"
    elif unique_code == "2212232323":
        print "type6"
    elif unique_code == "322142243434":
        print "type7"
    elif unique_code == "2223132322":
        print "type8"
    elif unique_code == "331332332333":
        print "type9"
    elif unique_code == "33314334334334":
        print "type10"
    elif unique_code == "222222333333":
        print "type11"
    elif unique_code == "42224222444444":
        print "type12"
    elif unique_code == "222242424242":
        print "type13"
    elif unique_code == "2222222222":
        print "type14"
    elif unique_code == "322322323233":
        print "type15"
    elif unique_code == "33224324324343":
        print "type16"
    elif unique_code == "33233233333333":
        print "type17"
    elif unique_code == "4332433244344344":
        print "type18"
    elif unique_code == "3333433433433433":
        print "type19"
    elif unique_code == "443344334433444444":
        print "type20"
    elif unique_code == "44444444444444444444":
        print "type21"
    else:
        print "Unknown type"
        print unique_code
        print neighbour_number
        print "\n"





motif_sampling(4, 2000)