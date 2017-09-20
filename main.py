import random

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

data_set = {}
source  = open("sample.txt", "r")

ID = ""
Adjacent = ""
for i in source.readlines():
    pos = 0
    while i[pos] != " ":
        ID = ID + i[pos]
        pos = pos + 1
    #print ID
    while i[pos] == " ":
        pos = pos + 1
    while i[pos] != " ":
        Adjacent = Adjacent + i[pos]
        pos = pos + 1
    #print (ID + " " + Adjacent)

    if ID in data_set.keys():
        Vertex.addNeighbor(data_set[ID], Adjacent, 1)
    else:
        data_set[ID] = Vertex(ID)
        Vertex.addNeighbor(data_set[ID], Adjacent, 1)

    if Adjacent in data_set.keys():
        Vertex.addNeighbor(data_set[Adjacent], ID, 1)
    else:
        data_set[Adjacent] = Vertex(Adjacent)
        Vertex.addNeighbor(data_set[Adjacent], ID, 1)

    #print data_set[ID].connectedTo.keys()
    ID = ""
    Adjacent = ""
    # Here we reset the value of ID and Adjacent values
    #print length

total_nodes =  len (data_set.keys())
#for key, values in data_set.items():
    #print (values.id)
    #print (key)
    #print values.id
    #print values.connectedTo.keys()
    #print (Vertex.getConnections(values))
source.close()

#data_list = data_set.keys()
#print len(data_list)

#print length
def size_three_motif ():
    open_triangle = 0
    close_triangle = 0
    for i in range(0, 5000):
        random1 = random.randint(0, total_nodes - 1)

        #randomly pick one data point from the ID list generated
        n1_key = data_set.keys()[random1]
        n1_node = data_set([n1_key])
        n1_len = len(Vertex.getConnections(n1_node))
        random2 = random.randint(0, n1_len - 1)
        while (random2 == random1):
            random2 = random.randint(0, n1_len - 1)
        n2_key = Vertex.getConnections(n1_node)[random2]
        n2_node = data_set.values([n2_key])
        n2_len = len(Vertex.getConnections(n2_node))
        if (n2_len == 1):
            open_triangle = open_triangle + 1
        else:
            random3 = random.randint(0, n2_len - 1)
            while random3 == random1 or random3 == random2:
                random3 = random.randint(0, n2_len - 1)
        n3_key = Vertex.getConnections(n2_node)[random3]
        n3_node = data_set.values([n3_key])
        print n1_key + " " + n2_key + " " + n3_key


size_three_motif ()
