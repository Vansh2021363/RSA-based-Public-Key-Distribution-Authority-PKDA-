import socket
import pickle
import RSA

PU={"4000": "(103,187)", "4001": "(17,3233)", "4002": "(11,259)"}
PR_PKDA=7
PU_PKDA=103
n_PKDA=187

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname
host = socket.gethostname()

# Define the port on which you want to connect
port = 4000

# Bind to the port
server_socket.bind((host, port))

# Now wait for client connection
server_socket.listen(5)

while True:
    # Establish connection with client
    client_socket, addr = server_socket.accept()
    print('Got request from', addr)

    # Receive the data from client
    data = client_socket.recv(1024).decode()

    print ("Received request: ", end="")
    print (data)

    lst = data.split('|')
    id_A = lst[0].strip()

    response = PU[id_A] +"|" + data

    encrypted_response = RSA.encrypt_algo(response, PR_PKDA, n_PKDA)

    byte_response = pickle.dumps(encrypted_response)

    client_socket.send(byte_response)

    print("Response sent encrypted with private key of PKDA: ", end="")
    print (encrypted_response)

    # Close the connection with client
    client_socket.close()
