import socket
import pickle
import RSA
import re
import datetime
import random

tem=random.randint(1, 1000)
N2=str(tem)


current_time = datetime.datetime.now()

PR_B=59
PU_B=11
n_B=259
PU_PKDA=103
PKDA_port=4000
n_PKDA=187

ClientA_port=4001

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname
host = socket.gethostname()

# Define the port on which you want to connect
port = 4002

# Bind to the port
server_socket.bind((host, port))

# Now wait for client connection
server_socket.listen(5)




# Establish connection with client
client_socket, addr = server_socket.accept()
print('Got connection from', addr)
# Receive the data from client
data = client_socket.recv(1024)
# Unpickle the received data (convert back to Python object)
received_list = pickle.loads(data)
print("Received list:", received_list)
data=RSA.decrypt_algo(received_list, PR_B, n_B)
print("Decrypted message with private key of B: ", end="")
print(data)

#Extract id of A and N1 from the above decrypted message
pq = data.split('|')
ID_A= pq[0].strip()
N1=pq[1].strip()

message_B_PKDA=ID_A+"|"+ current_time.strftime("%H:%M:%S")

PKDA_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PKDA_socket.connect((host, PKDA_port))

print("ClientB sends request to PKDA: ", end="")
print(message_B_PKDA)
PKDA_socket.sendall(message_B_PKDA.encode())

response_1=pickle.loads(PKDA_socket.recv(1024))

print("Encrypted public key of Client A from PKDA encrypted with public key of PKDA: ", end="")
print(response_1)

#calculate public key of a

PU_A=[]

temp=RSA.decrypt_algo(response_1, PU_PKDA, n_PKDA)
lst = temp.split('|')
first= lst[0].strip()
lst=first.split(',')
tempo=re.search(r'\d+', lst[0].strip()).group()
PU_A.append(int(tempo))

tempu=re.search(r'\d+', lst[1].strip()).group()
PU_A.append(int(tempu))

print(PU_A)

ClientA_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientA_socket.connect((host, ClientA_port))


message_BA=N1+"|"+N2
print("Message sent to A: ", end="")
print(message_BA)
encrypted_message_BA=RSA.encrypt_algo(message_BA, PU_A[0], PU_A[1])
print("Encrypted message sent to A using public key of A")
print(encrypted_message_BA)
ClientA_socket.sendall(pickle.dumps(encrypted_message_BA))

response_2=pickle.loads(client_socket.recv(1024))
print("Encrypted response received: ", end="")
print (response_2)

decrypted_response_2=RSA.decrypt_algo(response_2, PR_B, n_B)
print("Decrypted response from A: ", end="")
print(decrypted_response_2)

response_2=pickle.loads(client_socket.recv(1024))
print("Encrypted response received: ", end="")
print (response_2)

decrypted_response_2=RSA.decrypt_algo(response_2, PR_B, n_B)
print("Decrypted response from A: ", end="")
print(decrypted_response_2)

encrypted_message_BA=RSA.encrypt_algo("Got-it1" + "|"+ current_time.strftime("%H:%M:%S"), PU_A[0], PU_A[1])
ClientA_socket.sendall(pickle.dumps(encrypted_message_BA))
print("Encrypted message sent to A using public key of A")
print(encrypted_message_BA)

response_2=pickle.loads(client_socket.recv(1024))
print("Encrypted response received: ", end="")
print (response_2)

decrypted_response_2=RSA.decrypt_algo(response_2, PR_B, n_B)
print("Decrypted response from A: ", end="")
print(decrypted_response_2)

encrypted_message_BA=RSA.encrypt_algo("Got-it2" + "|"+ current_time.strftime("%H:%M:%S"), PU_A[0], PU_A[1])
ClientA_socket.sendall(pickle.dumps(encrypted_message_BA))
print("Encrypted message sent to A using public key of A")
print(encrypted_message_BA)

response_2=pickle.loads(client_socket.recv(1024))
print("Encrypted response received: ", end="")
print (response_2)

decrypted_response_2=RSA.decrypt_algo(response_2, PR_B, n_B)
print("Decrypted response from A: ", end="")
print(decrypted_response_2)

encrypted_message_BA=RSA.encrypt_algo("Got-it3" + "|"+ current_time.strftime("%H:%M:%S"), PU_A[0], PU_A[1])
ClientA_socket.sendall(pickle.dumps(encrypted_message_BA))
print("Encrypted message sent to A using public key of A")
print(encrypted_message_BA)

# Close the connection with client
client_socket.close()