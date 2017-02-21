import json
import os
import shutil
from colorama import Fore
from .utils import find_main_directory
from .settings import FISH_HOOK_CONFIG_NAME, FISH_HOOK_CONFIG_CONTENT, PORT, HOST,\
    DEFAULT_EVENTS, SH_FILE_CONTENT, APP_CONFIG_NAME


class FishHook:
    def __init__(self, base_path=None):
        self.base_path = base_path or find_main_directory(os.getcwd())
        if not self.base_path:
            raise Exception('Application configuration is not existed!')

        self.config_path = os.path.join(self.base_path, FISH_HOOK_CONFIG_NAME)

    @staticmethod
    def get_secret(app_name):
        base_path = find_main_directory(os.getcwd())
        app_path = os.path.join(base_path, app_name)
        config_file_path = os.path.join(app_path, APP_CONFIG_NAME)
        if not (os.path.exists(app_path) or os.path.exists(config_file_path)):
            return None

        with open(config_file_path) as json_data_file:
            return json.load(json_data_file).get('secret', None)

    @staticmethod
    def execute_event(app_name, event):
        base_path = find_main_directory(os.getcwd())
        app_path = os.path.join(base_path, app_name)
        config_file_path = os.path.join(app_path, APP_CONFIG_NAME)
        event_file_path = os.path.join(app_path, event + '.sh')  # Event file path

        # Judge the app config file whether is existed
        if not os.path.exists(config_file_path):
            raise Exception('No any configuration file of {} is defined!'.format(app_name))

        # Judge the event file whether is existed
        if not os.path.exists(event_file_path):
            raise Exception('No any {} event is defined!'.format(event))

        os.system('sh ' + event_file_path)

    def run(self):
        # Check app config
        if not os.path.exists(self.config_path):
            raise Exception(Fore.RED + 'Application configuration is not existed!')

        # Read config file. todo: More free fields
        with open(self.config_path) as json_config_file:
            from .server import server

            config = json.load(json_config_file)
            host = config.get('host', HOST)
            port = config.get('port', PORT)
            self.apps = config.get('apps', []) # todo
            self._check_files_integrity()
            server.run(host=host, port=port)

    def init(self, port):
        # Create fish-hook directory
        port = port or PORT
        os.mkdir(self.base_path)
        os.chdir(self.base_path)

        # If config file is not existed, create it
        # Write fish-hook configuration in `main` directory
        if not os.path.exists(self.config_path):
            general_config_file = FISH_HOOK_CONFIG_CONTENT(port=port, host=HOST, apps=[])._asdict()
            with open(self.config_path, 'w') as outfile:
                json.dump(general_config_file, outfile) # Write general config file
        else:
            raise Exception('Application configuration has existed!')

    def remove(self, name):
        app_path = os.path.join(self.base_path, name)
        if not os.path.exists(app_path):
            raise Exception ('App directory is not existed!')
        # Read general config file
        config = self._get_general_config()
        if name not in config['apps']:
            raise Exception('fish-hook not includes this app!')

        config['apps'].remove(name)

        # Rewrite general config file
        self._write_general_config(config)

        # Remove the app directory
        shutil.rmtree(app_path)
        print(Fore.GREEN + '{} has been removed!'.format(name))

    def new(self, name, secret):
        app_path = os.path.join(self.base_path, name)
        config_file_content = {
            'name': name,
            'secret': secret
        }

        if os.path.exists(app_path):
            raise Exception('App directory is existed!')

        # Create app directory
        os.mkdir(app_path)

        # Write default webhook shell files in `app` directory. todo: Support more default event templates
        for event_name in DEFAULT_EVENTS:
            with open(os.path.join(app_path, event_name + '.sh'), 'w') as outfile:
                outfile.write(SH_FILE_CONTENT.format(name=name))

        # Read general config file
        config = self._get_general_config()
        config['apps'].append(name)

        # Rewrite general config file
        self._write_general_config(config)

        # Write app configuration in `app` directory
        with open(os.path.join(app_path, APP_CONFIG_NAME), 'w') as outfile:
            json.dump(config_file_content, outfile)

    def _check_files_integrity(self):
        miss_apps = set(self.apps).difference(set(os.listdir(self.base_path)))
        if len(miss_apps) != 0:
            raise Exception('Your missing apps: {}'.format(', '.join(miss_apps)))

    def _get_general_config(self, func=None):
        with open(os.path.join(self.base_path, FISH_HOOK_CONFIG_NAME)) as json_config_file:
            config = json.load(json_config_file)
            if not func:
                return config
            return func(config)

    def _write_general_config(self, content):
        # Write app configuration in `app` directory
        with open(self.config_path, 'w') as outfile:
            json.dump(content, outfile)
