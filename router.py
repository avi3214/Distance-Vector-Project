from collections import defaultdict 

# read the input file and parse into adjacency list 
def read_textfile(filename):
    with open(filename, 'r') as f:
        # read file and strip trailing whitespace 
        # split the nodes into lines 
        lines = f.read().strip().split("\n")   
       
    # create a defaultdict object  of type list 
    d = defaultdict(list)

    for line in lines: 
        # split the lines using a space as the delimiter 
        ls = line.split(" ")
        # create the adjacency list to store the network 
        d[ls[0]].append(ls[1:])
    #print(d)

# craete a table for each node 

def main():
    read_textfile('network.txt')

if __name__ == "__main__":
    main()
