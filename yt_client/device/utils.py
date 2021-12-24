RASPI_PLATFORM = 'Linux-5.10.63-v7+-armv7l-with-glibc2.31'
LAPTOP_PLATFORM = 'Linux-5.11.0-43-generic-x86_64-with-glibc2.29'

from platform import platform


def hardware() -> str:
    if 'armv7l' in platform():
        return "rpi"
    else:
        return "laptop"