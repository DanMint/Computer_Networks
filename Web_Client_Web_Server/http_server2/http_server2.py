import socket
import threading
import sys
import os

# Function to handle the client's request in a separate thread
def handle_client(client_socket, client_address):
    try:
        print(f"Connection from {client_address}")
        request = client_socket.recv(1024).decode()
        print(f"Request: {request}")

        # Parse the HTTP request to get the file path
        headers = request.split("\n")
        if len(headers) > 0:
            get_request = headers[0].split()
            if len(get_request) > 1:
                path = get_request[1]
                if path == '/':
                    path = "basics.html"

                file_path = f"data/{path}"

                # Check if the requested file exists and send its contents
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        content = file.read()
                    response = 'HTTP/1.1 200 OK\n\n' + content
                else:
                    response = 'HTTP/1.1 404 Not Found\n\nFile Not Found'
            else:
                response = 'HTTP/1.1 400 Bad Request\n\nBad Request'
        else:
            response = 'HTTP/1.1 400 Bad Request\n\nBad Request'

        client_socket.sendall(response.encode())
    finally:
        client_socket.close()

# Function to start the server
def start_server(port):
    # Create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", port)

    # Bind the socket to the address and port
    server_socket.bind(server_address)

    # Listen for incoming connections with a backlog of 5
    server_socket.listen(5)
    print(f"Server is listening on localhost:{port}")

    # Main loop to accept connections and start new threads for each client
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Main function to start the server with the specified port
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 http_server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)

if __name__ == "__main__":
    main()
