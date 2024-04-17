network = {}

# read the input file and parse into adjacency list 
def read_textfile(filename):
    with open(filename, 'r') as f:
        for line in f:
            node, neighbor, cost = map(int, line.strip().split())
            #print(node, neighbor, cost)
            
            if node not in network:
                #print(f"Adding node {node} to network")
                network[node] = {}
                for i in range(1,6):
                    if i == node:
                        network[node][i] = 0
                    else:
                        network[node][i] = 99
            network[node][neighbor] = cost
            
            if neighbor not in network:
                #print(f"Adding node {neighbor} to network")
                network[neighbor] = {}
                for i in range(1,6):
                    if i == neighbor:
                        network[neighbor][i] = 0
                    else:
                        network[neighbor][i] = 99
            network[neighbor][node] = cost

    return network

def update_network(node, dv_table):
    pass


def main():
    read_textfile('network.txt')

    print("\nInitial network:")
    for node, dv_table in network.items():
        print(f"\nNode {node}: {dv_table}")
    print("\nPress enter to continue")

    # create a loop until the network reaches a stable state 
    # in loop, update the distance vector until network reaches stable
    stable_state = False 
    while not stable_state:
        inp = input()
        if inp == 'q':
            break

        for node, dv_table in network.items():
            update_network(node, dv_table)
        
        for node, dv_table in network.items():
            print(f"\nNode {node}: {dv_table}")
        input("\nPress enter to continue")
    

if __name__ == "__main__":
    main()
