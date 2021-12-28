# Display must be initalized before fan. The GPIO Initialisation takes splace in the foreign display library
import logging
from datetime import datetime

from pathlib import Path
from yaml import safe_load

from yt_client.common import Info
from yt_client.loop import Loop

LOG = logging.getLogger(__name__)


def setup_logger(logfile_path: Path):
    logging.basicConfig(
        filename=f"{logfile_path}/{datetime.now().strftime('%Y-%m-%d_%H-%M')}.log",
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(name)s: %(message)s',
        datefmt='%m.%d.%Y %H:%M:%S'
    )


if __name__ == '__main__':
    with open('hmi/yt_client/config.yml', 'r') as f:
        cfg = safe_load(f)

    setup_logger(Path('hmi/yt_client')/Path(cfg["logging"]["logfile_location"]))
    LOG.debug("Starting up!")

    info = Info(log_data=True, datalogfile_location=cfg["logging"]["datalogfile_location"])
    l = Loop(cfg['loop'], info)
    l.start()
