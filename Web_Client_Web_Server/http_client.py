import socket  
import sys     

def url_parse(url):
    scheme = ""
    host = ""
    port = ""
    path = ""
    query = ""
    fragment = ""

    # here I'm getting the scheme part of the URL
    pos = 0
    while True:
        if url[pos] == ':':
            pos += 3
            break
        
        scheme += url[pos]
        pos += 1

    ended = False
    # here I get the host and port
    in_port_section = False
    while True:
        if pos == len(url):
            ended = True
            break

        elif url[pos] == '/':
            pos += 1
            break
        
        elif url[pos] == ":":
            in_port_section = True

        elif in_port_section:
            port += url[pos]

        else:
            host += url[pos]
        
        pos += 1

    if scheme == "http" and port == "":
        port = "80"

    elif scheme == "https" and port == "":
        port = "443"

    elif scheme == "ftp" and port == "":
        port = "21"

    if ended:
        return [scheme, host, port, path, query, fragment]

    # here I get the path
    while True:
        if pos == len(url):
            ended = True
            break

        elif url[pos] == "?":
            pos += 1
            break
        
        path += url[pos]
        pos += 1

    if ended:
        return [scheme, host, port, path, query, fragment]

    # here I get the query
    while True:
        if pos == len(url):
            ended = True
            break

        elif url[pos] == "#":
            pos += 1
            break
        
        query += url[pos]
        pos += 1
    
    if ended:
        return [scheme, host, port, path, query, fragment]

    # here I get the fragment 
    while True:
        if pos == len(url):
            ended = True
            break

        fragment += url[pos]
        pos += 1
    
    return [scheme, host, port, path, query, fragment]
    
def create_and_connect_socket(host, port):
    # Initialization of socket
    try:
        # Create a socket object using IPv4 and TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connection to the server
        s.connect((host, int(port)))
        return s
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def request(host, path):
    if not path:
        path = "/"
    elif not path.startswith("/"):
        path = "/" + path
    return f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"


def get_the_body(website_response):
    delimiter = "<"
    index = website_response.find(delimiter) - 1
    print(website_response[index + len(delimiter):])


def main():
    url = ""

    if len(sys.argv) > 1:
        url = sys.argv[1]
            
    else:
        print("No arguments were passed.")
        sys.exit(1)

    # parsing the URL
    scheme, host, port, path, query, fragment = url_parse(url)

    # creating the socket
    client_socket = create_and_connect_socket(host, port)
    
    request_str = request(host, path)

    # Send the HTTP GET request
    client_socket.sendall(request_str.encode())

    # Receive the response
    # intialized a byte string
    response = b""
    while True:
        # reciving upto 4096 bytes of data
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        response += chunk

    # Close the socket
    client_socket.close()

    # Print the response (for now, print the full response to understand it)
    website_response = response.decode()

    get_the_body(website_response)


if __name__ == "__main__":
    main()
