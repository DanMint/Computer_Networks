import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port to connect to
    server_address = ('127.0.0.1', 8000)
    
    # Connect to the server
    print(f"Connecting to {server_address[0]} on port {server_address[1]}")
    client_socket.connect(server_address)
    
    try:
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        
        # Receive data from the server
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
    finally:
        # Close the connection
        print("Closing connection")
        client_socket.close()

if __name__ == "__main__":
    start_client()
