import socket 
import threading

"""
create a thread for each node
set up a client and server so each node can act as each
"""
HOST = socket.gethostname()

def server_setup():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the socket object
    
    server_socket.bind((HOST, 1234))
    server_socket.listen(5)

    while True:
        conn, addr = server_socket.accept()
         
def client_setup():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4567
    client_socket.connect((HOST, port))
    client_socket.sendall()
    data = client_socket.recv(1024)




# read the input file and parse into adjacency list 
def read_textfile(filename):
    network = {} 

    with open(filename, 'r') as f:
        for line in f:
            node, neighbor, cost = map(int, line.strip().split())
            #print(f"Processing line: {node}, {neighbor}, {cost}")
            
            if node not in network:
                #print(f"Node {node} not in network, adding.")
                network[node] = {n: 99 if n != node else 0 for n in range(1, 6)}
            else:
                network[node][neighbor] = cost

            # Add reverse edge as well (assuming bidirectional links)
            if neighbor not in network:
                #print(f"Node {neighbor} not in network, adding.")
                network[neighbor] = {n: 99 if n != neighbor else 0 for n in range(1, 6)}
            else:
                network[neighbor][node] = cost


            #print(f"Current network: {network}")

    return network


def main():
    network = read_textfile('network.txt')
    for node, dv_table in network.items():
        print(f"Node {node}: {dv_table}")

    for node in network.items():
        pass
      

if __name__ == "__main__":
    main()
