import click
from colorama import Fore, Back, Style
from .app import FishHook
from .settings import EVENTS_TEXT, GET_STARTED_INFO


@click.group()
def main():
    pass

@main.command()
@click.argument('directory', nargs=-1, type=click.Path(exists=False))
@click.option('--port', prompt='port', help='Fish-hook server will run on this host which belongs to http://0.0.0.0')
def init(directory, port):
    directory_name = (len(directory) == 0 and 'fish' or directory[0])
    hook = FishHook(port=port)
    hook.init(directory_name)
    create_initialization_info(directory_name)

@main.command()
@click.option('--name', prompt='repository name', help='The repository name')
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

def create_initialization_info(directory_name):
    print(GET_STARTED_INFO.format(
        fore_black=Fore.BLACK, back_green=Back.GREEN, fore_white=Fore.WHITE, fore_reset=Fore.RESET, back_reset=Back.RESET,
        style_bright=Style.BRIGHT, style_normal=Style.NORMAL, fore_green=Fore.GREEN,
        dir_name='fish-hook'
    ))