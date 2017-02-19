import click
import os
from .app import FishHook
from .settings import EVENTS_TEXT

@click.group()
def main():
    pass

@main.command()
@click.argument('directory', nargs=-1, type=click.Path(exists=False))
@click.option('--port', prompt='port', help='Fish-hook server will run on this host which belongs to http://0.0.0.0')
def init(directory, port):
    if len(directory) == 0:
        directory = 'fish-hook'
    dir_path = os.path.join(os.getcwd(), directory)
    os.mkdir(dir_path)
    os.chdir(dir_path)
    hook = FishHook(port=port)
    hook.init()
    print('Next: enter {} directory and new some hooks!'.format(directory))

@main.command()
@click.option('--name', prompt='webhook name', help='The webhook name of this application')
@click.option('--secret', prompt='webhook secret', help='As same as the secret in github webhook page')
def new(name, secret):
    hook = FishHook()
    hook.create(name, secret)

@main.command()
def server():
    hook = FishHook()
    hook.run()

@main.command()
def remove():
    # todo
    pass

@main.command()
def events():
    print(EVENTS_TEXT)
