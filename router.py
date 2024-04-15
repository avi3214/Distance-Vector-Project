import socket 
import threading

"""
create a thread for each node
set up a client and server so each node can act as each
"""
HOST = socket.gethostname()
PORT = 5050
network = {}

def server_setup(node):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT+node))
        s.listen()
        conn, addr = s.accept()
        with conn:
            #print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
    conn.close()

         
def client_setup(node):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT+node))
            s.sendall(data)
            data = s.recv(1024)
    except Exception as e:
        print(f"Exception occurred in client_setup for node {node}: {e}")

# read the input file and parse into adjacency list 
def read_textfile(filename):
    with open(filename, 'r') as f:
        for line in f:
            node, neighbor, cost = map(int, line.strip().split())
            #print(node, neighbor, cost)
            
            if node not in network:
                print(f"Adding node {node} to network")
                network[node] = {}
                for i in range(1,6):
                    if i == node:
                        network[node][i] = 0
                    else:
                        network[node][i] = 99
            network[node][neighbor] = cost
            
            if neighbor not in network:
                print(f"Adding node {neighbor} to network")
                network[neighbor] = {}
                for i in range(1,6):
                    if i == neighbor:
                        network[neighbor][i] = 0
                    else:
                        network[neighbor][i] = 99
            network[neighbor][node] = cost

    return network

def create_threads():
    threads = []
    for node in network.keys():
        server_threads = threading.Thread(target=server_setup, args=(node, ))
        client_threads = threading.Thread(target=client_setup, args=(node, ))
        
        threads.append(server_threads)
        threads.append(client_threads)

        server_threads.start()
        client_threads.start()

    for thread in threads:
        thread.join()

def main():
    read_textfile('network.txt')
    create_threads()
    for node, dv_table in network.items():
        print(f"Node {node}: {dv_table}")

if __name__ == "__main__":
    main()
