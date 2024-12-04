import socket
import pickle
import RSA
import re
import datetime
import random

current_time = datetime.datetime.now()
tem=random.randint(1, 1000)
N1=str(tem)

PR_A=2753
PU_A=17
n_A=3233
PU_PKDA=103
n_PKDA=187

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname
host = socket.gethostname()

# Define the port on which you want to connect
port = 4001
ClientB_port=4002
PKDA_port=4000

# Bind to the port
server_socket.bind((host, port))

# Now wait for client connection
server_socket.listen(5)

PKDA_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PKDA_socket.connect((host, PKDA_port))

first_request="4002" +"|"+ current_time.strftime("%H:%M:%S")
print("ClientA sends request to PKDA: ", end="")
print(first_request)
PKDA_socket.sendall(first_request.encode())

response_1=pickle.loads(PKDA_socket.recv(1024))

print("Encrypted public key of Client B from PKDA encrypted with public key of PKDA: ", end="")
print(response_1)


PU_B=[]


temp=RSA.decrypt_algo(response_1, PU_PKDA, n_PKDA)
lst = temp.split('|')
first= lst[0].strip()
lst=first.split(',')
tempo=re.search(r'\d+', lst[0].strip()).group()
PU_B.append(int(tempo))

tempu=re.search(r'\d+', lst[1].strip()).group()
PU_B.append(int(tempu))


#calculate public key of b

ClientB_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientB_socket.connect((host, ClientB_port))

message_AB= "4001|"+N1
encrypted_message_AB = RSA.encrypt_algo(message_AB, PU_B[0], PU_B[1])

ClientB_socket.sendall(pickle.dumps(encrypted_message_AB))

print("First message sent to Client B encrypted with public key of B: ", end="")
print(encrypted_message_AB)

# Establish connection with client
client_socket, addr = server_socket.accept()
print('Got connection from', addr)
# Receive the data from client
data = client_socket.recv(1024)
# Unpickle the received data (convert back to Python object)
received_list = pickle.loads(data)
print("Received list:", received_list)
data=RSA.decrypt_algo(received_list, PR_A, n_A)
print("Decrypted message with private key of A: ", end="")
print(data)

tempi=data.split('|')
N2=data[1].strip()
print("N2: ", end="")
print(N2)

encrypted_message_AB=RSA.encrypt_algo(N2, PU_B[0], PU_B[1])
ClientB_socket.sendall(pickle.dumps(encrypted_message_AB))
print("message of N2 sent to Client B encrypted with public key of B: ", end="")
print(encrypted_message_AB)

message_AB="Hi1" + "|"+ current_time.strftime("%H:%M:%S")
encrypted_message_AB=RSA.encrypt_algo(message_AB, PU_B[0], PU_B[1])
ClientB_socket.sendall(pickle.dumps(encrypted_message_AB))
print("message of N2 sent to Client B encrypted with public key of B: ", end="")
print(encrypted_message_AB)

data = client_socket.recv(1024)
received_list= pickle.loads(data)
print("Received list:", received_list)
data=RSA.decrypt_algo(received_list, PR_A, n_A)
print("Decrypted message with private key of A: ", end="")
print(data)

message_AB="Hi2" + "|"+ current_time.strftime("%H:%M:%S")
encrypted_message_AB=RSA.encrypt_algo(message_AB, PU_B[0], PU_B[1])
ClientB_socket.sendall(pickle.dumps(encrypted_message_AB))
print("message of N2 sent to Client B encrypted with public key of B: ", end="")
print(encrypted_message_AB)

data = client_socket.recv(1024)
received_list= pickle.loads(data)
print("Received list:", received_list)
data=RSA.decrypt_algo(received_list, PR_A, n_A)
print("Decrypted message with private key of A: ", end="")
print(data)

message_AB="Hi3" + "|"+ current_time.strftime("%H:%M:%S")
encrypted_message_AB=RSA.encrypt_algo(message_AB, PU_B[0], PU_B[1])
ClientB_socket.sendall(pickle.dumps(encrypted_message_AB))
print("message of N2 sent to Client B encrypted with public key of B: ", end="")
print(encrypted_message_AB)

data = client_socket.recv(1024)
received_list= pickle.loads(data)
print("Received list:", received_list)
data=RSA.decrypt_algo(received_list, PR_A, n_A)
print("Decrypted message with private key of A: ", end="")
print(data)