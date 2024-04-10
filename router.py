# read the input file and parse into adjacency list 
def read_textfile(filename):
    network = {} 
    node_list = []

    with open(filename, 'r') as f:
        for line in f:
            node, neighbor, cost = map(int, line.strip().split())
            #print(node, neighbor, cost)
            # keeping track of every node 
            if node not in node_list:
                node_list.append(node)
            if neighbor not in node_list:
                node_list.append(neighbor)

    # now that we have every node, create a dv_table for each node 
            network.setdefault(node, {})[neighbor] = {'cost': cost, 'next_hop': None}
    
    for node in node_list: 
        network[node] = {}
        for neighbor, cost in network.get(node, []):  # Check if node exists in adjacency list
            network[node][neighbor] = {'cost': cost, 'next_hop': None}


    return network

def main():
    network = read_textfile('network.txt')
    for node, dv_table in network.items():
        print(f"Node {node}: {dv_table}")


if __name__ == "__main__":
    main()
