import csv                     # for reading the file
import numpy as np             # for dealing with arrays 


def out_in_link(row , out_link , in_link , n=0):
    s_node = int(row[0])
    destination  = int(row[1])
    out_link[s_node-1] += 1   # add one to the number of outgoing links (source node-1 , for the index of the file is more than the index of links )
    in_link[destination-1].add(s_node-1)    # add source node to this destination 
    return out_link , in_link

def url_link(row , urls):     # storing all the nodes with links in a systematic way
    ind = int(row[0])
    urls[ind] = row[1]
    return urls

 


link_data = open("hollins.dat" , "r")     # store the first line which has the no of nodes and edges 
reader = csv.reader(link_data , delimiter = ' ', skipinitialspace=True)
row = next(reader)         # reads the first line 

nodes = int(row[0])
edges = int(row[1])

#create a dic variable .
urls = {}
initialvector = []                # intial value for all the links 

# create a list storing the no of outgoing links with each nodes 
out_link = [0 for i in range(nodes)]


# create a set to store the no of incoming links with each nodes ; set for not taking the duplicate one   
in_link = [set() for i in range(nodes)]
sorted_rank = []

# page rank set initially of all the pages 
pg_rank = np.zeros((nodes,nodes))

for i in range(nodes):
    row = next(reader)
    urls  = url_link(row ,urls)
    initialvector.append(1/nodes)
   

   
    

for n in range(edges) :  
    row = next(reader)
    out_link , in_link = out_in_link( row , out_link , in_link ) 


for i in range(nodes) :   
    for j in in_link[i] :
        pg_rank[i][j] = 1/out_link[j]   # only care about the pages having an outgoing links (according to the theorem)


# for storing the ranks of the page till the ranks stop changing 
# n stored the no of iteration to be held , sice the links are more than 5000, therefore n will iterate for 1000 time
n = 0
damp = .85   # .85 is the default damp value 
length = len(initialvector)
vector = [0] * length 
while  n <1000 :
    vector = [0] * length        # vector to store the page rank from initial (1) to the final(n) times .
    for i in range(length):
        ti = 0
        for j in in_link[i]:
            ti += initialvector[j]*(pg_rank[i][j])   
        vector[i] = (1-damp) + damp*ti
    initialvector = vector.copy()
    n += 1



   
for i in range(len(vector)) :
    sorted_rank.append((vector[i], i))
sorted_rank.sort()      # ranks from min to max   
sorted_rank.reverse()           


with open("total_rank.txt", "w") as file :     # storing the links with rank from min to max in a text file 
    for i in sorted_rank :
        Rank = i[0]
        index = i[1] + 1
        row = str(index) + "\t  Rank: " + str(Rank) + '    ' + urls[index] + '\n'   
        file.write(row)
    

