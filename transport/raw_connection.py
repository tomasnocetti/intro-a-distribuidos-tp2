import socket
import logging


class RawConnection:
    def __init__(self, socket, destination_address):
        self.socket = socket
        self.destination_address = destination_address

    def send_segment(self, segment):
        logging.debug(f'L> {repr(segment)}')
        self.socket.sendto(segment.serialize(), self.destination_address)