import threading
import unittest
import socket
import json
import io
import sys


import server


def start_server(serv):
    client = serv.accept()
    serv.create_handler(client)
    serv.join()
    serv.close()


class TestServer(unittest.TestCase):
    def setUp(self):
        self.old_stdout = sys.stdout
        self.my_stdout = io.StringIO()
        sys.stdout = self.my_stdout

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_start_tcp_server(self):
        serv = server.Server(0, 0, '127.0.0.1', 7777)
        serv_thread = threading.Thread(target=start_server, args=(serv,))
        serv_thread.start()

        fake_client = socket.socket()
        fake_client.settimeout(1)
        fake_client.connect(('127.0.0.1', 7777))
        fake_client.recv(1)
        fake_client.close()

        serv_thread.join()

    def test_server_request_handle(self):
        serv = server.Server(10, 7, '127.0.0.1', 8888)
        serv_thread = threading.Thread(target=start_server, args=(serv,))
        serv_thread.start()

        fake_client = socket.socket()
        fake_client.settimeout(5)
        fake_client.connect(('127.0.0.1', 8888))
        fake_client.recv(1)

        fake_client.send(json.dumps('wrong_url_sdhfk384ehfhsdgcfs.com').encode())
        data = json.loads(fake_client.recv(1024).decode())
        self.assertEqual(type(data), str)  # str - error message

        fake_client.send(json.dumps('https://github.com/').encode())
        data = json.loads(fake_client.recv(1024).decode())
        self.assertEqual(data, {'GitHub': 35, 'and': 42, 'for': 26, 'the': 27, 'to': 29, 'with': 26, 'your': 31})

        fake_client.close()

        serv_thread.join()

        self.assertEqual(self.my_stdout.getvalue(), 'Success urls: 0\tFailure urls: 1\n'
                                                    'Success urls: 1\tFailure urls: 1\n')


if __name__ == '__main__':
    unittest.main()
