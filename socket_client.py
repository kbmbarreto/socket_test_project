import socket

def send_socket_command(host, port, message):
    try:
        with socket.create_connection((host, port), timeout=5) as s:
            s.sendall((message + '\n').encode())
            return s.recv(1024).decode().strip()
    except Exception as e:
        return f"ERROR: {e}"