import socket

LOCALHOST = "127.0.0.1"
PORT = 8089

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Сервер ")
print("Waiting for client request..")

clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''
array = []
while True:
    data = clientConnection.recv(1024)
    msg = data.decode()
    if msg == 'Over':
        print("Соединение прервано")
        break

    print("Equation is recievied")
    operation_list = msg.split()
    result = ''
    if len(operation_list) == 3:
        result = 0

        first_num = operation_list[0]
        operation = operation_list[1]
        second_num = operation_list[2]

        num1 = int(first_num)
        num2 = int(second_num)

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "*":
            result = num1 * num2
        array.append(result)
        output = str(result)
        clientConnection.send(output.encode())
    elif len(operation_list) == 1:
        if operation_list[0] == 'history':
            result = ''
            for i in array:
                result = result +' ' + str(i)
            output = result
            clientConnection.send(output.encode())
        else:
            output = 'i dont know what is this'
            clientConnection.send(output.encode())

clientConnection.close()





