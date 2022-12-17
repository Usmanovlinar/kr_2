import socket

SERVER = "127.0.0.1"
PORT = 8089

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))

while True:
    print("Пример ввода : 4 + 5")
    enter = input("Enter the operation in \ the form opreand operator oprenad: ")

    if enter == "Over":
        break

    client.send(enter.encode())

    answer = client.recv(1024)
    print("Ответ: " + answer.decode())
    print("Наберите 'Over' для завершения")

client.close()