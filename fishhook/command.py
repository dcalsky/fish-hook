import click
import os
from colorama import Fore, Back, Style
from .fishhook import FishHook
from .settings import EVENTS_TEXT, GET_STARTED_INFO, MAIN_DIRECTORY_NAME


@click.group()
def main():
    pass

@main.command()
@click.argument('directory', nargs=-1, type=click.Path(exists=False))
@click.option('--port', prompt='port', help='Fish-hook server will run on this host which belongs to 0.0.0.0')
def init(directory, port):
    directory_name = (len(directory) == 0 and MAIN_DIRECTORY_NAME or directory[0])
    base_path = os.path.join(os.getcwd(), directory_name)
    hook = FishHook(base_path=base_path)
    hook.init(port=port)
    create_initialization_info(directory_name)

@main.command()
@click.option('--name', prompt='repository name', help='The repository name')
@click.option('--secret', prompt='webhook secret(optional)', default='', help='As same as the secret in github webhook page')
def new(name, secret):
    hook = FishHook()
    hook.new(name, secret)

@main.command()
def server():
    hook = FishHook()
    hook.run()

@main.command()
@click.option('--name', prompt='repository name', help='The repository name')
def remove(name):
    hook = FishHook()
    hook.remove(name)

@main.command()
def events():
    print(EVENTS_TEXT)

def create_initialization_info(directory_name):
    print(GET_STARTED_INFO.format(
        fore_black=Fore.BLACK, back_green=Back.GREEN, fore_white=Fore.WHITE, fore_reset=Fore.RESET, back_reset=Back.RESET,
        style_bright=Style.BRIGHT, style_normal=Style.NORMAL, fore_green=Fore.GREEN,
        dir_name=directory_name
    ))
