from collections import namedtuple

PORT = '2333'
HOST = '0.0.0.0'
MAIN_DIRECTORY_NAME = 'fish'
APP_CONFIG_NAME = 'app_config.json'
FISH_HOOK_CONFIG_NAME = 'config.json'
DEFAULT_EVENTS = ['push']
FISH_HOOK_CONFIG_CONTENT = namedtuple('fish_config', ['host', 'port', 'apps'])
REQUIRED_HEADERS = [ 'x-github-event', 'x-github-delivery' ]

APP_DESC = r"""
     _____ _     _       _                 _
    |  ___(_)___| |__   | |__   ___   ___ | | __
    | |_  | / __| '_ \  | '_ \ / _ \ / _ \| |/ /
    |  _| | \__ \ | | | | | | | (_) | (_) |   <
    |_|   |_|___/_| |_| |_| |_|\___/ \___/|_|\_\


"""

GET_STARTED_INFO = r"""
    {fore_black}{back_green} SUCCESS {fore_reset}{back_reset} Your new webhooks manager project has been successfully generated in {dir_name}!

    {fore_white}{style_bright}To get started:

    {fore_reset}{style_normal}cd {dir_name}
    fish-hook new
    {style_bright}EDIT THE WEBHOOK CONFIG...
    {fore_reset}{style_normal}fish-hook server
    {style_bright}{fore_green}

    {fore_white}{style_bright}In the production:

    {fore_reset}{style_normal}OPEN THE FIREWALL PORT(Such as port: 2333)...
    {fore_reset}{style_normal}sudo firewall-cmd --zone=public --add-port=2333/tcp --permanent
    {fore_reset}{style_normal}screen -d -m fish-hook server

""" + APP_DESC

SH_FILE_CONTENT = r"""
#!/usr/bin/env bash

APP_PATH="$HOME/{name}"

echo "Open the app directory"
cd $APP_PATH
echo "Pulling source code..."
git clean -f
git pull
echo "Finished"
"""

EVENTS_TEXT = """
    "*": "Any time any event is triggered",
    "commit_comment": "Any time a Commit is commented on",
    "create": "Any time a Repository, Branch, or Tag is created",
    "delete": "Any time a Branch or Tag is deleted",
    "deployment_status": "Any time a deployment for the Repository has a status update from the API",
    "deployment": "Any time a Repository has a new deployment created from the API",
    "fork": "Any time a Repository is forked",
    "gollum": "Any time a Wiki page is updated",
    "issue_comment": "Any time an Issue is commented on",
    "issues": "Any time an Issue is opened or closed",
    "member": "Any time a User is added as a collaborator to a non-Organization Repository",
    "membership": "Any time a User is added or removed from a team. Organization hooks only.",
    "page_build": "Any time a Pages site is built or results in a failed build",
    "public": "Any time a Repository changes from private to public",
    "pull_request_review_comment": "Any time a Commit is commented on while inside a Pull Request review (the Files Changed tab)",
    "pull_request": "Any time a Pull Request is opened, closed, or synchronized (updated due to a new push in the branch that the pull request is tracking)",
    "push": "Any git push to a Repository. This is the default event",
    "release": "Any time a Release is published in the Repository",
    "repository": "Any time a Repository is created. Organization hooks only.",
    "status": "Any time a Repository has a status update from the API",
    "team_add": "Any time a team is added or modified on a Repository",
    "watchAny": "time a User watches the Repository"
"""
