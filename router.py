# read the input file and parse into adjacency list 
def read_textfile(filename):
    network = {} 

    with open(filename, 'r') as f:
        for line in f:
            node, neighbor, cost = map(int, line.strip().split())
            #print(f"Processing line: {node}, {neighbor}, {cost}")
            if node not in network:
                #print(f"Node {node} not in network, adding.")
                network[node] = {n: 0 if n == node else 99 for n in range(1,6)}
            else:
                network[node][neighbor] = cost

            # Add reverse edge as well (assuming bidirectional links)
            if neighbor not in network:
                #print(f"Node {neighbor} not in network, adding.")\
                network[neighbor] = {n: 0 if n == neighbor else 99 for n in range(1,6)}
            else:
                network[neighbor][node] = cost

            #print(f"Current network: {network}")

    return network

def main():
    network = read_textfile('network.txt')
    for node, dv_table in network.items():
        print(f"Node {node}: {dv_table}")
        #Wpass

if __name__ == "__main__":
    main()
