class Env:
    def __init__(self, env: str):
        self.env = env

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value: str):
        self._env = value