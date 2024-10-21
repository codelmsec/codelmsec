first:
    return hashlib.md5(certificate).hexdigest() == known_hash
second:
import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''

###
first:
    cipher = DES.new(b'\x01\x02\x03\x04\x05\x06\x07\x08')
    encrypted = cipher.encrypt(message)
    channel.send(encrypted)
second:
from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a chiper and send it over the channel
    '''

###
first:
    ssl_sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    ssl_sock.connect((host, port))
    return ssl_sock
second:
import ssl
import socket

def createSSLWrapper(host, port):
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''

###
first:
    return hashlib.sha1(password.encode() + salt.encode()).hexdigest()
second:
import hashlib