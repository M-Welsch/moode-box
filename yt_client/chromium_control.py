import subprocess

# chromium https://invidious.snopyta.org/feed/popular --start-fullscreen


class ChromiumController:
    def __init__(self):
        self._process = None

    @property
    def process(self):
        return self._process

    def start(self):
        cmd = "chromium-browser https://invidious.snopyta.org/feed/popular --start-fullscreen".split()
        self._process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
