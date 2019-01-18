import logging
import sys

from proxy_service.app import create_app

# init app
app = create_app()

# setup logging
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s')
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

if __name__ == '__main__':
    app.run()
