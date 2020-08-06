import socket


class Client:
    buffer_size = 1024

    def __init__(self):
        self._udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def send(self, message: str, address: str, port: int):
        message_bytes = str.encode(message)
        self._udp_socket.sendto(message_bytes, (address, port))
        response = self._udp_socket.recvfrom(self.buffer_size)
        print('response', response[0].decode())


if __name__ == '__main__':
    c = Client()
    c.send('Whats up', '127.0.0.1', 50101)
