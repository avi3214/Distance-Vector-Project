import time 

network = {}
# read the input file and parse network into an adjacency list 
# adjacency list is stored inside a dictionary 
def read_textfile(filename):
    with open(filename, 'r') as f:
        for line in f:
            # stores text file input into respective nodes and their costs 
            node, neighbor, cost = map(int, line.strip().split())   
            #print(node, neighbor, cost)
            
            # stores the each node as keys 
            # nodes neighbors are sorted into an adjacency list 
            if node not in network:
                #print(f"Adding node {node} to network")
                network[node] = {}
                # sets the cost of node to itself to 0 
                # sets costs of all other nodes to arbitary cost
                for i in range(1,6):
                    if i == node:
                        network[node][i] = 0
                    else:
                        network[node][i] = 99
            network[node][neighbor] = cost
            
            # captures any neighbor not listed as a node 
            # and stores it in the network as a node 
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

# function takes in current node and updates its distance vector table 
def update_network(node, dv_table):
    # create copy of original vector table to compare later 
    new_distance_vector = network[node].copy()
    
    # checks to see if the neighbors are the node itself or non-neighbors 
    # if they are, skip them and focus on the neighbors nodes 
    for neighbor, cost in dv_table.items():
        if neighbor == node or cost == 99:
            continue 

        # looks at the neighbors nodes and calculates path from node passed in to non-neighbors 
        for neighbors_nodes, neighbors_nodes_cost in network[neighbor].items():
            new_cost = network[node][neighbor] + neighbors_nodes_cost

            # cost between nodes is updated if shorter path is calculated 
            if new_cost < new_distance_vector[neighbors_nodes]:
                new_distance_vector[neighbors_nodes] = new_cost

    network[node] = new_distance_vector

def run_manually():
    print("Initial network:")
    for node, dv_table in network.items():
        print(f"Node {node}: {dv_table}")
    print("\nPress enter to continue")

    # for neighbor, cost in dv_table.items():
    #     print(f"NEIGHBOR {neighbor} COST {cost}")

    # create a loop until the network reaches a stable state 
    # in loop, update the distance vector until network reaches stable
    stable_state = False 
    while not stable_state:
        #initialize old network for comparison later 
        old_network = {} 
        for node, dv_table in network.items():
            old_network[node] = dv_table.copy()

        # allows user to quit program 
        inp = input()
        if inp == 'q':
            break
        
        # pass in the nodes to the distance vector algorithm 
        for node, dv_table in network.items():
            update_network(node, dv_table)

        # stable state is reached if there are no new updates to the network 
        for node, dv_table in network.items():
            if network[node] != old_network[node]:
                break
            else:
                stable_state = True
        
        print("\nCurrent network")
        for node, dv_table in network.items():
            print(f"Node {node}: {dv_table}")
        input("\nPress enter to continue")

    print("Stable state achieved")   

def run_automatically():
    start_time = time.time()
    stable_state = False 
    while not stable_state:
        #initialize old network for comparison later 
        old_network = {} 
        for node, dv_table in network.items():
            old_network[node] = dv_table.copy()
            
        # pass in the nodes to the distance vector algorithm 
        for node, dv_table in network.items():
            update_network(node, dv_table)

        # stable state is reached if there are no new updates to the network 
        for node, dv_table in network.items():
            if network[node] != old_network[node]:
                break
            else:
                stable_state = True
            
        print("\nCurrent network")
        for node, dv_table in network.items():
            print(f"Node {node}: {dv_table}")
            
        end_time = time.time()
            
    print("Stable state achieved")  

    elapsed_time = (end_time - start_time) * 1000
    print("Execution time:", elapsed_time, "milliseconds")    

def main():
    read_textfile('network.txt')
    
    print("\nPress a then press enter for the program to run automatically or m then press enter to run manually")
    user_choice = input()
    if user_choice == 'm':
        run_manually()
    elif user_choice == 'a':
        run_automatically()

if __name__ == "__main__":
    main()
