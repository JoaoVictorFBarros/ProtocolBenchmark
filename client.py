import socket
import time

def generate_large_message(size=32 * 1024):
    """Gera uma mensagem grande para teste."""
    return 'X' * size

def test_tcp_client(host='127.0.0.1', port=65432, num_requests=10):
    message = generate_large_message()
    times = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for _ in range(num_requests):
            start_time = time.time()
            s.sendall(message.encode())
            s.recv(len(message))
            end_time = time.time()
            times.append(end_time - start_time)
    return times

def test_udp_client(host='127.0.0.1', port=65433, num_requests=10):
    message = generate_large_message()
    times = []
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        for _ in range(num_requests):
            start_time = time.time()
            s.sendto(message.encode(), (host, port))
            s.recvfrom(len(message))
            end_time = time.time()
            times.append(end_time - start_time)
    return times

def print_statistics(times, protocol):
    if times:
        total_time = sum(times)
        print(f'Estatísticas de {protocol}:')
        print(f'  Soma dos tempos de resposta: {total_time:.4f} segundos')
        print(f'  Total de requisições: {len(times)}')
    else:
        print(f'Nenhum dado para {protocol}')

if __name__ == "__main__":
    num_requests = 100000
    print("Iniciando testes TCP...")
    tcp_times = test_tcp_client(num_requests=num_requests)
    print("Iniciando testes UDP...")
    udp_times = test_udp_client(num_requests=num_requests)

    print_statistics(tcp_times, "TCP")
    print_statistics(udp_times, "UDP")
