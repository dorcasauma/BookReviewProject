from http import client
import socket

from httpx import request
def server(host, port):
    """
    Write code that starts server on host proviced and port. 
    """
    listening_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    listening_socket.bind((host,port))
    listening_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    listening_socket.listen(5)
    print ("starting server")
    while True:
        client_connection, client_address = listening_socket.accept()
        request_data = client_connection.recv(1024)
        print(f"request data:{request_data.decode()}")
        html_page = """
        <html>
            <body>
                <h1>HELLO WORLD</h1>
            </body>
        </html>
        """
        
        client_connection.sendall(
            f"HTTP/1.1 200 OK/n/nhello world".encode()
        )
        client_connection.close()
        print("done serving the request")
if __name__ == '__main__':
    server('127.0.0.1',8000)