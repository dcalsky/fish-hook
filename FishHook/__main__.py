import logging
import click
from app import FishHook

logger = logging.getLogger(__name__)

APP_DESC = """ @author: dcalsky """
__version__ = '0.0.1'


@click.command()
@click.option('--port', prompt='Port',
              help='Webhook will run on this host which belongs to http://0.0.0.0')
@click.option('--secret', prompt='Secret',
              help='Webhook will run on this host which belongs to http://0.0.0.0')
def command(port, secret):
    hook = FishHook(port=2333, host='0.0.0.0', secret=secret)

if __name__ == '__main__':
    command()
