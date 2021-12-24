# Display must be initalized before fan. The GPIO Initialisation takes splace in the foreign display library

from yt_client.loop import Loop
from yt_client.chromium_control import ChromiumController

if __name__ == '__main__':
    cc = ChromiumController()
    cc.start()

    l = Loop()
    l.start()
