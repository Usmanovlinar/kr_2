import socket

LOCALHOST = "127.0.0.1"
PORT = 8094

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Часть сервера запущена... ")

clientConnection, clientAddress = server.accept()
msg = ''
array = []



while True:
    data = clientConnection.recv(1024)
    msg = data.decode()
    ans = eval(msg)
    ans = str(ans)
    clientConnection.send(ans.encode())



clientConnection.close()