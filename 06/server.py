import collections
import sys
import threading
import queue
import socket
import json
from urllib.request import urlopen


def get_flag_val(flag):
    if flag in sys.argv:
        flag_ind = sys.argv.index(flag) + 1
        if flag_ind < len(sys.argv):
            return int(sys.argv[flag_ind])


def parse_text(text):
    words = []
    stage = 0
    cur_str = []
    for char in text:
        if stage == 0:
            if char in ('\n', '\a', '\b', '\v', '\f', '\0', '\r', '\t', ' ', '<'):
                if len(cur_str) > 0:
                    words.append(''.join(cur_str))
                if char == '<':
                    stage = 1
                cur_str = []
            else:
                cur_str.append(char)
        elif stage == 1:
            if char == '>':
                cur_str = []
                stage = 0
    return words


def process_url(url, words_count):
    if not url.startswith('https://'):
        url = f'https://{url}'

    while url[-1] in ('\n', '\a', '\b', '\v', '\f', '\0', '\r', '\t', ' '):
        url = url[:-1]

    html = urlopen(url).read().decode()
    words = parse_text(html)
    c = collections.Counter(words)
    most_common_dict = {elem[0]: elem[1] for elem in c.most_common(words_count)}
    return most_common_dict


class Server:
    @staticmethod
    def target_to_work(requests_q, words_count, url_processed_callback):
        while True:
            try:
                client, url = requests_q.get(timeout=1)
                success = True
                try:
                    data = process_url(url, words_count)
                except Exception as ex:
                    data = str(ex)
                    success = False

                client.send(json.dumps(data).encode())
                url_processed_callback(success)
                requests_q.task_done()
            except Exception:
                pass

    @staticmethod
    def target_to_handle(client, requests_q):
        while True:
            data = client.recv(1024).decode()
            if not data:
                break
            requests_q.put((client, json.loads(data)))
        client.close()

    def __init__(self, workers_count, words_count, ip, port):
        self.success_count = 0
        self.failure_count = 0
        self.workers_count = workers_count
        self.words_count = words_count
        self.requests_q = queue.Queue()
        self.workers = [
            threading.Thread(target=Server.target_to_work,
                             args=(self.requests_q,
                                   self.words_count,
                                   lambda success: (self.update_stat(success), self.Stats())),
                             daemon=True)
            for _ in range(workers_count)
        ]
        for thread in self.workers:
            thread.start()

        self._sock = socket.socket()
        self._sock.bind((ip, port))
        self._sock.listen()

        self.client_handles = []

    def update_stat(self, success=True):
        with threading.Lock():
            if success:
                self.success_count += 1
            else:
                self.failure_count += 1

    def create_handler(self, client):
        client_handler = threading.Thread(target=Server.target_to_handle,
                                          args=(client, self.requests_q),
                                          daemon=True)
        self.client_handles.append(client_handler)
        client_handler.start()

    def join_client_handler(self):
        for thread in self.client_handles:
            thread.join()

    def join_workers(self):
        self.requests_q.join()

    def join(self):
        self.join_workers()
        self.join_client_handler()

    def Stats(self):
        print(f'Success urls: {self.success_count}\t', end='')
        print(f'Failure urls: {self.failure_count}\n', end='')

    def accept(self):
        client, _ = self._sock.accept()
        client.send(b'1')
        return client

    def close(self):
        self._sock.close()


def main():
    workers_count = get_flag_val('-w')
    if not workers_count:
        workers_count = 10
    common_words_count = get_flag_val('-k')
    if not common_words_count:
        common_words_count = 7
    ip = socket.gethostbyname(socket.gethostname())
    port = get_flag_val('-p')
    if not port:
        port = 99999

    server = Server(workers_count, common_words_count, ip, port)

    try:
        while True:
            client = server.accept()
            server.create_handler(client)
    except KeyboardInterrupt:
        server.close()


if __name__ == '__main__':
    main()
