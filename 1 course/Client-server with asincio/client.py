import socket
import time


class ClientError(BaseException):
    pass


def check_data(data):
    if len(data) != 3:
        return False
    try:
        int(data[2])
        float(data[1])
    except ValueError:
        return False

    return True


def string_processing(data_list):
    res = {}
    if data_list[0] == "ok":
        if data_list[1] == "":
            return {}
        for i in range(1, len(data_list) - 1):
            if data_list[i] == "":
                continue
            d = data_list[i].split(' ')
            if not check_data(d):
                raise ClientError
            if d[0] in res:
                res[d[0]].append((int(d[2]), float(d[1])))
            else:
                res[d[0]] = list()
                res[d[0]].append((int(d[2]), float(d[1])))
    else:
        raise ClientError

    for key in res:
        res[key].sort()
    return res


class Client:

    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._timeout = timeout
        self.sock = socket.create_connection((host, port), timeout)

    def get(self, key):
        self.sock.send("get {}\n".format(key).encode("utf8"))
        byte_data = self.sock.recv(1024)
        data = byte_data.decode("utf8")
        data_list = data.split('\n')
        return string_processing(data_list)

    def put(self, key, value, timestamp=None):
        if timestamp is None:
            self.sock.send("put {} {} {}\n".format(key, value, int(time.time())).encode("utf8"))
        else:
            self.sock.send("put {} {} {}\n".format(key, value, timestamp).encode("utf8"))
        byte_data = self.sock.recv(1024)
        data = byte_data.decode("utf8")
        data_list = data.split('\n')

        if data_list[0] == "error":
            raise ClientError(data_list[1])
        elif data_list[0] == "ok":
            pass
        else:
            raise ClientError

    def __del__(self):
        self.sock.close()
