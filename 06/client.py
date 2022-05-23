import sys
import threading
import queue
import socket
import json


from server import get_flag_val


class Client:
    @staticmethod
    def thread_target(ip, port, url_queue):
        soc = socket.socket()
        soc.connect((ip, port))
        soc.recv(1)
        while True:
            try:
                url = url_queue.get(timeout=1)
                soc.send(json.dumps(url).encode())
                data = soc.recv(1024).decode()
                if not data:
                    break
                url_queue.task_done()
                print(f'{url}: {json.loads(data)}\n', end='')
            except Exception:
                pass
        soc.close()
        url_queue.task_done()

    def __init__(self, threads_count, ip, port):
        self._threads_count = threads_count
        self._url_queue = queue.Queue()
        self._ip = ip
        self._port = port
        self._threads = [
            threading.Thread(target=Client.thread_target,
                             args=(self._ip, self._port, self._url_queue),
                             daemon=True)
            for _ in range(self._threads_count)
        ]
        for thread in self._threads:
            thread.start()

    def handle(self, url):
        self._url_queue.put(url.strip())

    def join(self):
        self._url_queue.join()


def main():
    urls_fn = sys.argv[-1]
    threads_count = get_flag_val('-t')
    if not threads_count:
        threads_count = 10
    ip = get_flag_val('-i')
    if not ip:
        ip = '127.0.0.0'
    port = get_flag_val('-p')
    if not port:
        port = 99999

    client = Client(threads_count, ip, port)

    with open(urls_fn, 'r') as urls_file:
        for url in urls_file:
            client.handle(url)

    client.join()


if __name__ == '__main__':
    main()
