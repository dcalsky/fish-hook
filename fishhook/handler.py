import os
import json
from .settings import CONFIG_NAME, SH_FILE_CONTENT, DEFAULT_EVENTS


class Handler(object):
    def __init__(self, name, secret=None):
        self.name = name
        self.dir = os.getcwd()
        self.secret = secret
        self.app_path = os.path.join(self.dir, self.name)
        self.config_file_path = os.path.join(self.app_path, CONFIG_NAME)

        if secret is None:
            with open(self.config_file_path) as json_data_file:
                self.config_file = json.load(json_data_file)

    @property
    def config(self):
        return self.config_file

    def create(self):
        app_dir = os.path.join(self.dir, self.name)
        if os.path.exists(app_dir):
            raise Exception('App directory is existed!')

        os.mkdir(app_dir)
        config_file_content = {'name': self.name, 'secret': self.secret}

        # Write default webhook shell files in `app` directory. todo: Support more default event templates
        for event_name in DEFAULT_EVENTS:
            with open(os.path.join(app_dir, event_name + '.sh'), 'w') as outfile:
                outfile.write(SH_FILE_CONTENT.format(name=self.name))

        # Write app configuration in `app` directory
        with open(os.path.join(app_dir, CONFIG_NAME), 'w') as outfile:
            json.dump(config_file_content, outfile)

    def launch(self, event):
        files = [file for file in os.listdir(self.app_path)]
        # Get all events are defined in `app` directory
        current_events = map(lambda file: os.path.splitext(file)[-1] == '.json', files)
        if event in current_events:
            raise Exception('No any {} event is defined!'.format(event))

        os.system('sh ' + os.path.join(self.app_path, event + '.sh'))
