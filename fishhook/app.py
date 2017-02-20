from .server import server
from .settings import FISH_HOOK_CONFIG_NAME, FISH_HOOK_CONFIG_CONTENT, PORT, HOST
from .handler import Handler
import json
import os


class FishHook(object):
    def __init__(self, port=None, host=None):
        self.port = port
        self.host = host

    def run(self):
        config_path = os.path.join(os.getcwd(), FISH_HOOK_CONFIG_NAME)
        if not os.path.exists(config_path):
            raise Exception('Application configuration is not existed!')

        # Read config file. todo: More freedom fields
        with open(config_path) as json_config_file:
            config = json.load(json_config_file)
            self.host = config.get('host', HOST)
            self.port = config.get('port', PORT)

        server.run(host=self.host, port=self.port)

    def init(self, directory_name):
        # Create fish-hook directory
        dir_path = os.path.join(os.getcwd(), directory_name)
        os.mkdir(dir_path)
        os.chdir(dir_path)
        config_path = os.path.join(os.getcwd(), FISH_HOOK_CONFIG_NAME)
        # If config file is not existed, create it
        # Write fish-hook configuration in `main` directory
        if not os.path.exists(config_path):
            general_config_file = FISH_HOOK_CONFIG_CONTENT(port=self.port or PORT, host=self.host or HOST)._asdict()
            # circus_config_path = os.path.join(dir_path, CIRCUS_CONFIG_NAME)
            with open(config_path, 'w') as outfile:
                json.dump(general_config_file, outfile) # Write general config file
            # with open(circus_config_path, 'w') as outfile:
            #     outfile.write(CIRCUS_CONFIG_CONTENT) # Write circus config file
        else:
            raise Exception('Application configuration has existed!')

    def create(self, name, secret):
        handler = Handler(name, secret)
        handler.create()
