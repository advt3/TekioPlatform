import socket


class Server:
    ip_address = '127.0.0.1'
    local_port = 50101
    buffer_size = 1024
    _response = str.encode('received')

    def __init__(self):
        self._udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._udp_server_socket.bind((self.ip_address, self.local_port))

    def start(self):
        print('Server Ready')
        while True:
            bytes_pair = self._udp_server_socket.recvfrom(self.buffer_size)
            message = bytes_pair[0]
            client_address = bytes_pair[1]
            print('Message:', message.decode(), ' Client Address', client_address)
            self._udp_server_socket.sendto(self._response, client_address)


if __name__ == '__main__':
    s = Server()
    s.start()
