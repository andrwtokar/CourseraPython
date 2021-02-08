import asyncio


class StringConverter:
    tread_data = dict()

    def __init__(self, data):
        self.error = False
        data_list = (data.split('\n'))[0].split()
        if not data_list:
            data_list.append("error")
            self.error = True
        self.command = data_list[0].strip()

        if self.command == "get":
            if len(data_list) == 2:
                self.data = data_list[1].strip()
            else:
                self.error = True
        elif self.command == "put":
            if len(data_list) == 4:
                self.data = [data_list[1].strip()]
                try:
                    self.data.append(float(data_list[2].strip()))
                    self.data.append(int(data_list[3].strip()))
                except ValueError:
                    self.error = True
            else:
                self.error = True
        else:
            self.error = True

    def process(self):
        res = "ok\n"
        if self.error:
            res = "error\nwrong command\n"

        elif self.command == "put":
            if self.data[0] in StringConverter.tread_data.keys():
                work_list = StringConverter.tread_data[self.data[0]]
                for i in work_list:
                    if i[0] == self.data[2]:
                        work_list.remove(i)
            else:
                StringConverter.tread_data[self.data[0]] = []

            StringConverter.tread_data[self.data[0]].append((self.data[2], self.data[1]))

        elif self.data in StringConverter.tread_data.keys():
            for value in StringConverter.tread_data[self.data]:
                res += str(self.data) + " " + str(value[1]) + ' ' + str(value[0]) + '\n'

        elif self.data == "*":
            if not StringConverter.tread_data:
                res = "ok\n"
            else:
                for key in StringConverter.tread_data.keys():
                    for value in StringConverter.tread_data[key]:
                        res += key + " " + str(value[1]) + ' ' + str(value[0]) + '\n'

        return res + "\n"


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        res = StringConverter(data.decode())
        self.transport.write(res.process().encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
