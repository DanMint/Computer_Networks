import socket

def create_and_connect_socket(host, port):
    # Step 1: Initialize the socket
    try:
        # Create a socket object using IPv4 and TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Socket created to connect to {host} on port {port}")
        
        # Step 2: Connect to the server
        s.connect((host, port))
        print(f"Successfully connected to {host} on port {port}")
        
        return s
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# Example usage
host = 'example.com'
port = 80
socket = create_and_connect_socket(host, port)
