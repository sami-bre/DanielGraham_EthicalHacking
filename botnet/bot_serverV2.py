import socketserver

command = ""
with open('commands.txt', 'r') as file:
    command = file.readline()  # reading a single command on the first line
    command = command[:-1]


class BotHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        self.request.sendall(command.encode())
        res = (self.request.recv(2048)).decode()
        print("result from bot at {} - {} : ".format(self.client_address[0], self.client_address[1]))
        print(res)


if __name__ == "__main__":
    HOST, PORT = "", 8000
    tcpserver = socketserver.TCPServer((HOST, PORT), BotHandler)
    try:
        print("Waiting for bots to connect and executing [{}] as soon as they do ...".format(command))
        tcpserver.serve_forever()
    except:
        print("There was an error.")
