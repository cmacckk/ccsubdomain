import socket
from src.log import logger

def get_ip_address(domain):
    try:
        address = socket.getaddrinfo(domain, 'http')
        return address[0][4][0]
    except socket.gaierror as socket_gaierror:
        logger.debug(socket_gaierror)
        return None