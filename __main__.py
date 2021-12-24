# Display must be initalized before fan. The GPIO Initialisation takes splace in the foreign display library

from yt_client.loop import Loop


if __name__ == '__main__':
    l = Loop()
    l.start()
