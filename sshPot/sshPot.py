import paramiko
import socket
import threading
import io
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
import traceback


privkey = ed25519.Ed25519PrivateKey.generate()
pubkey = privkey.public_key()
serializedPrivKey = privkey.private_bytes(Encoding.PEM, PrivateFormat.OpenSSH, NoEncryption())
print(type(serializedPrivKey))
print(serializedPrivKey[:50])

class Server(paramiko.ServerInterface):
    def __init__(self, ip):
        self.ip = ip
        self.even = threading.Event

    def check_auth_password(self, username, password):
        #Grabs credentials
        print(f"[{self.ip}] attempt: {username} : {password}")
        with open("ssh_honeypot.log", "a") as f:
            f.write(f"{username}:{password} from {self.ip}\n")
        return paramiko.AUTH_FAILED #never goes through

    def check_channel_request(self, kind, chanid):
        if kind == "session": #open only nomral shell, no forwarding
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    

def connection(sock, addr):
    try:
        trans = paramiko.Transport(sock)
        key = paramiko.Ed25519Key.from_private_key(io.StringIO(serializedPrivKey.decode('utf-8')))
        trans.add_server_key(key)

        server = Server(addr[0])
        trans.start_server(server=server)
    except Exception as e:
        print("bs type shi")
        print(f"Error handling {addr}: {e}")
        traceback.print_exc()
    finally:
        trans.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 20))
sock.listen(100)
print("Listening on 10.**.***.*:20")

while True:
    print("bout to accept")
    print(sock)
    sock2, addr = sock.accept()
    print(addr)
    print("accepted")
    print(f"Connection from {addr}")
    threading.Thread(target=connection, args=(sock2, addr)).start()