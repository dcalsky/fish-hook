from .server import server
from .settings import FISH_HOOK_CONFIG_NAME, FISH_HOOK_CONFIG_CONTENT, PORT, HOST
from .handler import Handler
import json
import os


class FishHook(object):
    def __init__(self, port=None, host=None):
        dir_path = os.getcwd()
        self.config_path = os.path.join(dir_path, FISH_HOOK_CONFIG_NAME)
        self.port = port
        self.host = host

    def run(self):
        if not os.path.exists(self.config_path):
            raise Exception('Application configuration is not existed!')

        # Read config file. todo: More freedom fields
        with open(self.config_path) as json_config_file:
            config = json.load(json_config_file)
            self.host = config.get('host', HOST)
            self.port = config.get('port', PORT)

        server.run(host=self.host, port=self.port)

    def init(self):
        # If config file is not existed, create it
        # Write fish-hook configuration in `main` directory
        if not os.path.exists(self.config_path):
            config_file = FISH_HOOK_CONFIG_CONTENT(port=self.port or PORT, host=self.host or HOST)._asdict()
            with open(self.config_path, 'w') as outfile:
                json.dump(config_file, outfile)
        else:
            raise Exception('Application configuration has existed!')

    def create(self, name, secret):
        handler = Handler(name, secret)
        handler.create()
