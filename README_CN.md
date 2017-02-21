
fish-hook
=======
>一站式高效管理你多个github webhook.



## 背景

等你辛苦建立好了静态博客，却依然要忍受每次本地更新后，**还要ssh到远程重新git pull一遍的痛苦。**

当你终于用webhook handler写了一堆代码来解决这个应用的部署问题后，你依然发现，还有许许多多的项目等着你为它们写部署代码。

要是有一个集成化的工具，在一个目录里帮我管理所有的webhook就好了！fish-hook就是为此诞生的，它最大的特色就是：极力缩短开发者花在配置上的时间，约定大于配置。



## 开始使用
### 安装
安装python3.5或更高版本，再用pip包管理工具安装fish-hook
```bash
$ pip3 install fish-hook
```
### 新建fish-hook目录
```
$ fish-hook init
```
ssh进入远程主机后，运行该命令，并且设置一个通用的端口，例如: 2333。这样就创建了名为`fish`的目录，这是控制所有webhook的总目录。`$ cd fish`进入该目录。

### 接收端: 为一个仓库创建webhook
```
$ fish-hook new
```

假如你在github上开通了一个名为`blog`的仓库，并且打算为其开通webhook来实现自动部署。那么就输入`blog`以及你要为此webhook设定的密钥。
完成后，`blog`的webhook接收端就部署好了。


### 发送端: 在github上创建webhook
首先打开仓库的github设置页面，然后创建github webhook，填入基本信息。
可以注意到`Payload URL`这一栏，前面的IP地址就是你`远程主机的外网IP地址`，之后是你刚刚设置的端口，斜杆后就是`blog`目录，**与接收端的名字相同**。
密钥一栏当然也要与在fish-hook上设置的相同。

![webhook](https://camo.githubusercontent.com/c5d4b2208bc11a1db6afe95ada348a990b4d0c8f/687474703a2f2f7374617469632e6e6f64646c2e6d652f316430313036353332313930393762336166373631636461336461353565356236393862623737652d653734383330336363386563336134343637313137616437663133306565313266383830623465332e706e67)


### 设置接受push事件后的动作
假设你使用`git push`推送了新的内容到blog仓库，如何执行特定的shell脚本呢？
此时的fish-hook目录是这样的:
```
fish/
	config.json
	blog/
		app_config.json
		push.sh
```

为什么有一个push.sh文件呢？就这意味着，当你仓库接受新的push事件后，fish-hook就会运行`push.sh`这个shell脚本，里面的内容完全可以自己设置。

这就是所谓的`约定大于配置`，webhook接受到什么样的命令，就会运行`相同名字`的shell脚本，当然前提是你的目录里要存在这个脚本。

### 上线
```
$ fish-hook server
```
fish-hook为你封装了部署所需的web server。一条命令即可启动，此时所有的webhook都会被启用。

### 开启2333端口
centos默认开启了端口防火墙，如果你使用了一些具备安全组的云主机服务，**也需要开放所有安全组哦。**
```bash
$ sudo firewall-cmd --zone=public --add-port=2333/tcp --permanent
```

## 生产环境
### 使用Screen
```
screen -d -m fish-hook server
```
在`fish-hook`主目录运行该命令，即可使fish-hook server持久运行下去。

## webhook 事件们
[events](https://github.com/dcalsky/fish-hook#events)

## 更多帮助
请查看github仓库[fish-hook](https://github.com/dcalsky/fish-hook)
