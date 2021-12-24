# Display must be initalized before fan. The GPIO Initialisation takes splace in the foreign display library
from yaml import safe_load

from yt_client.loop import Loop
from yt_client.chromium_control import ChromiumController

if __name__ == '__main__':
    cc = ChromiumController()
    cc.start()

    with open('hmi/yt_client/config.yml', 'r') as f:
        cfg = safe_load(f)

    l = Loop(cfg['loop'])
    l.start()
