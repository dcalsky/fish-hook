
fish-hook
=================
fish-hook is an efficient tool for managing your lots of github webhooks.

[中文版文档](https://github.com/dcalsky/fish-hook/blob/master/README_CN.md)

## Requirement
- \>= python3.5
- pip3

*Notice: Because of using sanic web framework, python3.5 or more high version needed!*

## Get started
### Installation
```bash
$ pip3 install fish-hook
```

### Usage
```bash
$ fish-hook init
$ cd fish/
$ fish-hook new
```
Then edit shell scripts...
```bash
$ fish-hook server
```

If you create webhook for repository named `example`, `fish-hook` will create a subdirectory in main directory that the `structure` likes this:
```
fish/
	config.json
	example/
		app_config.json
		push.sh
```
You can reference [all webhook events of github](#events) add your own shell script file like `push.sh` in `example` directory.  

For example, if you create a shell script file named `fork.sh` in `example` directory,  the `fork.sh` will be executed when `fish-hook` got the `fork` event from github(someone forks this repository).

*The fish-hook will do nothing without send a normal message at `Ping ` event received.*

*Most of the time, you just need a shell script to handle `push` event :P*

### Create a webhook
```
$ fish-hook new
```

### Remove the webhook
```
$ fish-hook remove
```

### Get all github webhook events
```
$ fish-hook events
```

## Production
### Use Screen

`screen -d -m fish-hook server`

### Set github webhook
* Open  `https://github.com/:account/:repository/settings/hooks`
* Click 'add webhook' ![add](http://static.noddl.me/be982e7fbc49945cc1202a09d0d8e72824e80433-979996fcd6978a98c507e49101d5546eeddc98f0.png)

* FIll your server name with port and repository name(as same as fish-hook)![config](http://static.noddl.me/1d010653219097b3af761cda3da55e5b698bb77e-e748303cc8ec3a4467117ad7f130ee12f880b4e3.png)


## Events

| Name                          | Description                              |
| ----------------------------- | ---------------------------------------- |
| "*"                           | "Any time any event is triggered",       |
| commit_comment                | "Any time a Commit is commented on",     |
| "create"                      | "Any time a Repository, Branch, or Tag is created", |
| "delete"                      | "Any time a Branch or Tag is deleted",   |
| "deployment_status"           | "Any time a deployment for the Repository has a status update from the API", |
| "deployment"                  | "Any time a Repository has a new deployment created from the API", |
| "fork"                        | "Any time a Repository is forked",       |
| "gollum"                      | "Any time a Wiki page is updated",       |
| "issue_comment"               | "Any time an Issue is commented on",     |
| "issues"                      | "Any time an Issue is opened or closed", |
| "member"                      | "Any time a User is added as a collaborator to a non-Organization Repository", |
| "membership"                  | "Any time a User is added or removed from a team. Organization hooks only.", |
| "page_build"                  | "Any time a Pages site is built or results in a failed build", |
| "public"                      | "Any time a Repository changes from private to public", |
| "pull_request_review_comment" | "Any time a Commit is commented on while inside a Pull Request review (the Files Changed tab)", |
| "pull_request"                | "Any time a Pull Request is opened, closed, or synchronized (updated due to a new push in the branch that the pull request is tracking)", |
| "push"                        | "Any git push to a Repository. This is the default event", |
| "release"                     | "Any time a Release is published in the Repository", |
| "repository"                  | "Any time a Repository is created. Organization hooks only.", |
| "status"                      | "Any time a Repository has a status update from the API", |
| "team_add"                    | "Any time a team is added or modified on a Repository", |
| "watchAny"                    | "time a User watches the Repository"     |

## Author
[Dcalsky](https://www.noddl.me/)

## Licence
MIT

## Todos
- Add `prod` command
- Improve compatibility
