from pickle import GET
import socket

def server(host, port):
    """
    Write code that starts server on host proviced and port. 
    """
    listening_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    listening_socket.bind((host,port))
    listening_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    listening_socket.listen(5)
    print ("starting server")
    print("port;", port)
    print("host: ", host)
    while True:
        client_connection, client_address = listening_socket.accept()
        request_data = client_connection.recv(1024).decode()
        print(f"request data:{request_data.encode()}")
        html_page = """
        <html>
            <head>
                <title>Bookreview</title>
            </head>
            <body>
                <h1>User registration</h1>
                <form>
                <label for="username">Username</label><br>
                <input type="text"id="usename,name="username"><br>
                
                <label for="password1">Password1</label><br>
                <input type="password"id="password,name="password1"><br>
                
                <label for="password2">Password2</label><br>
                <input type="password"id="password2,name="passsword2"><br>
                
                <label for="dateOfBirth">date of birth</label>,<br>
                <input type="date"id="dateOfBirth,name="dateOfBirth"><br>
                
                <input type="submit" id="submit">
                </form>
            </body>
        </html>
        """
        response_status = "200 OK"
        if request_data.startswith("GET /?username"):
            response_status ="301 moved Permanently\r\nLocation: /user/login"
        if request_data.startswith("GET /user/login"):
                html_page = """
                    <html>
                        <body>
                            <h1>You have successfully reistered</h1>
                        <body/>
                    <html/>
                """
        client_connection.sendall(
            f"HTTP/1.1 {response_status}\r\nContent-Length: {len(html_page)}\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n{html_page}".encode()
        )
        client_connection.close()
        print("done serving the request")
        
if __name__ == '__main__':
    server('127.0.0.1',8004)
    