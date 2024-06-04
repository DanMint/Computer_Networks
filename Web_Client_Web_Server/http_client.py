import socket  
import sys     
import re

def url_parse(url):
    scheme = ""
    host = ""
    port = ""
    path = ""
    query = ""
    fragment = ""

    # here im getting the scheme part of the url
    pos = 0
    while (True):
        if (url[pos] == ':'):
            pos += 3
            break
        
        scheme += url[pos]
        pos += 1

    ended = False
    # here i get the host and port
    in_port_section = False
    while (True):
        if (pos == len(url)):
            ended = True
            break

        elif (url[pos] == '/'):
            pos += 1
            break
        
        elif (url[pos] == ":"):
            in_port_section = True

        elif (in_port_section):
            port += url[pos]

        else:
            host += url[pos]
        
        pos += 1

    if (scheme == "http" and port == ""):
        port = "80"

    elif (scheme == "https" and port == ""):
        port = "443"

    elif (scheme == "ftp" and port == ""):
        port = "21"


    if (ended):
        return [scheme, host, port, path, query, fragment]

    # here i get the path
    while (True):
        if (pos == len(url)):
            ended = True
            break

        elif (url[pos] == "?"):
            pos += 1
            break
        
        path += url[pos]
        pos += 1

    if (ended):
        return [scheme, host, port, path, query, fragment]

    # here i get the query
    while (True):
        if (pos == len(url)):
            ended = True
            break

        elif (url[pos] == "#"):
            pos += 1
            break
        
        query += url[pos]
        pos += 1
    
    if (ended):
        return [scheme, host, port, path, query, fragment]

    # here i get the fragment 

    while (True):
        if (pos == len(url)):
            ended = True
            break

        elif (url[pos] == "#"):
            pos += 1
            break
        
        fragment += url[pos]
        pos += 1
    
    if (ended):
        return [scheme, host, port, path, query, fragment]
    
def create_and_connect_socket(host, port):
    # Initialization of socket
    try:
        # Create a socket object using IPv4 and TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connection to the server
        s.connect((host, port))
        return s
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    url = ""

    if len(sys.argv) > 1:
        url = sys.argv[1]
            
    else:
        print("No arguments were passed.")

    # parsing the url
    parsed_url = url_parse(url)

    # creating the socket
    socket = create_and_connect_socket(parsed_url[1], parsed_url[2])

    




if __name__ == "__main__":
    main()