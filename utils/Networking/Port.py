import os
import sys


class Port:
    def __init__(self, host="127.0.0.1", port=None):
        self.platform = sys.platform
        self.port = str(port)
        self.host = host

    def is_open(self):
        if self.port is None:
            return Exception('ERR! Please specify a port.')

        if self.platform == "Windows":
            return os.system("telnet " + self.host + " " + self.port) == 0

        return os.system("nc -zw10 " + self.host + " " + self.port) == 0
