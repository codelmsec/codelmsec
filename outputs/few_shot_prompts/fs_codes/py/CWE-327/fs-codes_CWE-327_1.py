first:
    return hashlib.sha1(password.encode() + salt.encode()).hexdigest()
second:
import hashlib

def get_password_hash(password: str, salt: str):
    '''
    return the hash of the password
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
    return hashlib.md5(certificate).hexdigest() == known_hash
second:
import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''

###
first:
    ssl_sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    ssl_sock.connect((host, port))
    return ssl_sock
second:
import ssl
import socket