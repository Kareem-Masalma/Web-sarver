# Shahd Wisam 1212840
# Masa Shaheen 1210635
# Kareem Masalma 1220535
from socket import *


# Function to open the file and read its content
def open_file(file_name):
    with open(file_name, 'rb') as f:
        cont = f.read()
    return cont


serverPort = 6060
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
# The server will keep listening to the client
while True:
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    try:
        # The server will receive the request from the client
        sentence = connectionSocket.recv(1024).decode()
        print('Received: ', sentence)
        split = sentence.split(" ")
        s = split[1].split("/")
        file = s[1]

        # The server will send the response to the client depends on the request and the wanted file
        if (sentence.startswith("GET / ") or file == "en" or file == "main_en.html"
                or file == "index.html"):
            connectionSocket.send(b'HTTP/1.1 200 OK\n')
            connectionSocket.send(b'Content-Type: text/html\n')
            connectionSocket.send(b'\n')
            connectionSocket.send(open_file('main_en.html'))

        elif file == "ar" or file == "main_ar.html":
            connectionSocket.send(b'HTTP/1.1 200 OK\n')
            connectionSocket.send(b'Content-Type: text/html\n')
            connectionSocket.send(b'\n')
            connectionSocket.send(open_file('main_ar.html'))

        elif file.__contains__(".css"):
            connectionSocket.send(b'HTTP/1.1 200 OK\n')
            connectionSocket.send(b'Content-Type: text/css\n')
            connectionSocket.send(b'\n')
            connectionSocket.send(open_file(file))

        elif file.__contains__(".html"):
            connectionSocket.send(b'HTTP/1.1 200 OK\n')
            connectionSocket.send(b'Content-Type: text/html\n')
            connectionSocket.send(b'\n')
            connectionSocket.send(open_file(file))

        elif file.startswith("get_image?image-in"):
            name = sentence.split("=")
            name = name[1].split(" ")[0]
            readFile = open_file(name)
            if name.__contains__(".jpg"):
                connectionSocket.send(b'HTTP/1.1 200 OK\n')
                connectionSocket.send(b'Content-Type: image/jpg\n')
                connectionSocket.send(b'\n')
                connectionSocket.send(readFile)
            elif name.__contains__(".png"):
                connectionSocket.send(b'HTTP/1.1 200 OK\n')
                connectionSocket.send(b'Content-Type: image/png\n')
                connectionSocket.send(b'\n')
                connectionSocket.send(readFile)

        elif file.__contains__(".jpg"):
            readFile = open_file(file)
            connectionSocket.send(b'HTTP/1.1 200 OK\n')
            connectionSocket.send(b'Content-Type: image/jpg\n')
            connectionSocket.send(b'\n')
            connectionSocket.send(readFile)

        elif file.__contains__(".png"):
            readFile = open_file(file)
            connectionSocket.send(b'HTTP/1.1 200 OK\n')
            connectionSocket.send(b'Content-Type: image/png\n')
            connectionSocket.send(b'\n')
            connectionSocket.send(readFile)

        elif file == "so":
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
            connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
            connectionSocket.send("\r\n".encode())

        elif file == "itc":
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
            connectionSocket.send("Location: https://itc.birzeit.edu/ \r\n".encode())
            connectionSocket.send("\r\n".encode())

        else:
            connectionSocket.send(b'HTTP/1.1 404 Not Found\n')
            connectionSocket.send(b'Content-Type: text/html\n')
            connectionSocket.send(b'\n')
            with open('error.html', 'rb') as file:
                content = file.read()
                connectionSocket.send(content + f"<p> ip: {ip} port: {port} </p>".encode())

        connectionSocket.close()
    # If the server failed to send the response, it will send a 404 error
    except Exception as e:
        connectionSocket.send(b'HTTP/1.1 404 Not Found\n')
        connectionSocket.send(b'Content-Type: text/html\n')
        connectionSocket.send(b'\n')
        with open('error.html', 'rb') as file:
            content = file.read()
            connectionSocket.send(content + f"<p> ip: {ip} port: {port} </p>".encode())
            connectionSocket.close()
