import paramiko
import socket
import threading

import logging
logging.basicConfig(level=logging.DEBUG)
paramiko.util.log_to_file("paramiko_debug.log")

key_path = "/home/vyrttz/.ssh/id_ed25519"

class Server(paramiko.ServerInterface):
    def __init__(self, ip):
        self.ip = ip
        self.even = threading.Event

    def auth(self, username, password):
        #Grabs credentials
        print(f"[{self.ip}] attempt: {username} : {password}")
        with open("ssh_honeypot.log", "a") as f:
            f.write(f"{username}:{password} from {self.ip}\n")
        return paramiko.AUTH_FAILED #never goes through

    def check_channel_request(self, kind, chanid):
        if kind == "session": #open only nomral shell, no forwarding
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def get_allowed_auths(self, username):
        return "password"

def connection(sock, addr):
    try:
        trans = paramiko.Transport(sock)
        key = paramiko.Ed25519Key.from_private_key_file(key_path)
        trans.add_server_key(key)

        server = Server(addr[0])
        trans.start_server(server=server)
    except Exception as e:
        print("bs type shi")
        printf(f"Error handling {addr}: {e}")
    finally:
        trans.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 50000))
sock.listen(5)
print("Listening on 0.0.0.0:50000")

while True:
    print("bout to accept")
    print(sock)
    sock2, addr = sock.accept()
    print(addr)
    print("accepted")
    print(f"Connection from {addr}")
    threading.Thread(target=connection, args=(sock2, addr)).start()