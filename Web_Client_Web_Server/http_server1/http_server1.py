import socket
import sys
import os

def accept_socket(port):
    # Create a socket (remember sockets need 1.address family 2.data)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Create host and port
    server_address = ("localhost", port)

    # Bind the socket to the server address and port
    s.bind(server_address)

    # Listen for incoming connections
    s.listen(1)
    print("Server is listening on 127.0.0.1:8000")

    while True:
        # Create the connection
        connection, client_address = s.accept()
        
        try:
            if connection:
                print(f"Connection ip:{client_address}")
                # Recive the data that is passed from client
                request = connection.recv(1024).decode()
                print(f"Request: {request}")

                # Get headers of the reuqest
                headers = request.split("\n")

                # Here I get the path to what is asked for
                if len(headers) > 0:
                    get_request = headers[0].split()
                    path = get_request[1]
                    if path == '/':
                        path = "basics.html"
                
                    file_path = f"data/{path}"

                    if os.path.exists(file_path):
                        with open(file_path, 'r') as file:
                            content = file.read()
                        
                        response = 'HTTP/1.1 200 OK\n\n' + content
                
                else:
                    response = 'HTTP/1.1 404 Not Found\n\nFile Not Found'
                 # Here I send the html code of the file
                connection.sendall(response.encode())

        finally:
            # Close connection
            connection.close()


def main():

    if sys.argv == 1:
        print("Did not provide the port")
        exit(1)

    port = int(sys.argv[1])

    accept_socket(port)

if __name__ == "__main__":
    main()
