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
    directory = (len(directory) == 0 and 'fish-hook' or directory[0])
    dir_path = os.path.join(os.getcwd(), directory)
    os.mkdir(dir_path)
    os.chdir(dir_path)
    hook = FishHook(port=port)
    hook.init()
    print('\x1b[6;30;42m' + 'Success: next run `cd {}` enter fish-hook main directory and create some webhooks!'.format(directory) + '\x1b[0m')

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
