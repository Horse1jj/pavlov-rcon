import socket

class PavlovRCON:
    def init(self, ip: str, port: int, password: str):
        self.ip = ip
        self.port = port
        self.password = password
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        self.send_command(self.password)  # Authenticate

    def send_command(self, command: str) -> str:
        if not self.socket:
            raise ConnectionError("Not connected to the server.")
        self.socket.sendall(command.encode("utf-8") + b"\n")
        return self.socket.recv(4096).decode("utf-8")

    def disconnect(self):
        if self.socket:
            self.socket.close()
            self.socket = None