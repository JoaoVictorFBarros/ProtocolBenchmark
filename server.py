import socket
import threading
import time

def handle_tcp_client(conn):
    try:
        while True:
            data = conn.recv(32 * 1024)
            if not data:
                break
            conn.sendall(data)
    except Exception as e:
        print(f'Erro no tratamento do cliente TCP: {e}')
    finally:
        conn.close()

def start_tcp_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Servidor TCP aguardando conexão em {host}:{port}')
        while True:
            conn, addr = s.accept()
            print(f'Conectado por {addr}')
            threading.Thread(target=handle_tcp_client, args=(conn,)).start()

def start_udp_server(host='127.0.0.1', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f'Servidor UDP aguardando mensagens em {host}:{port}')
        while True:
            data, addr = s.recvfrom(32 * 1024)
            s.sendto(data, addr)

if __name__ == "__main__":
    threading.Thread(target=start_tcp_server).start()
    threading.Thread(target=start_udp_server).start()
