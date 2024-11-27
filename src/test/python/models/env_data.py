class EnvData:
    def __init__(self, wait: int, host: str):
        self.wait = wait
        self.host = host

    @property
    def wait(self):
        return self._wait

    @wait.setter
    def wait(self, value: int):
        self._wait = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value: str):
        self._host = value
