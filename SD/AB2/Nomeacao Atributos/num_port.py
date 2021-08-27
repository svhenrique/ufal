class NumPort:

    num_port = 65433 - 100

    def _get_port(self):
        return self.num_port

    def _set_port(self):
        self.num_port += 1

    def return_new_port(self):
        port = self._get_port()
        self._set_port()
        return port


PORT = NumPort()
