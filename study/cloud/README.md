# 云端学习入口

固定地址：<https://kkozia.top/kalman/>。

## 用语

| 用语 | 含义 |
|---|---|
| 云端 | 腾讯云服务器上的 JupyterLab |
| 本地 | 本机仓库和本机 JupyterLab |
| 登录信息 | 固定密码和快捷登录令牌 |

## 阅读和运行

1. 在浏览器打开固定地址。
2. 首次访问时，输入登录密码。
3. 在左侧文件列表打开章节。
4. 选中代码单元后，按 **Shift+Enter**。
5. 按 **Ctrl+S** 保存修改。

登录页面只填写密码，无须用户名。
登录信息保存在服务器的 `/etc/kalman-study/`。
服务器重启后，服务自动启动。

| 章节 | 云端页面 |
|---|---|
| 中文第一章 | [g-h 滤波](https://kkozia.top/kalman/lab/tree/01-g-h-filter.zh-CN.ipynb) |
| 中文第二章 | [离散贝叶斯滤波](https://kkozia.top/kalman/lab/tree/02-Discrete-Bayes.zh-CN.ipynb) |
| 英文第一章 | [g-h Filter](https://kkozia.top/kalman/lab/tree/01-g-h-filter.ipynb) |
| 英文第二章 | [Discrete Bayes](https://kkozia.top/kalman/lab/tree/02-Discrete-Bayes.ipynb) |

本次部署复制了本地章节和现有修改。
之后，本地和云端分别保存修改。
两端没有自动同步。
重新上传前，必须先备份云端文件。

## 服务位置

| 项目 | 路径或名称 |
|---|---|
| SSH 连接 | `ssh tengxunyun` |
| 仓库副本 | `/opt/kalman-study` |
| Python 环境 | `/opt/kalman-study/.venv` |
| 服务账户 | `kalman-study` |
| 服务名称 | `kalman-study.service` |
| 服务配置 | `/etc/kalman-study/jupyter_server_config.py` |
| HTTPS 路由 | `/etc/nginx/kalman-study-location.conf` |
| 后端监听 | `127.0.0.1:8890` |

Nginx 使用现有域名的 HTTPS 证书。
`/kalman/` 路径转发到后端。
后端没有新增公网监听端口。

## 已验证

- 中文第一章的 52 个代码单元全部执行成功。
- 中文第二章的 38 个代码单元全部执行成功。
- 公网 HTTPS 登录页面正常打开。
- 固定密码登录和登录 Cookie 验证通过。
- 未登录的文件 API 返回拒绝访问。
- 公网 WebSocket 内核执行和绘图验证通过。
- 服务已启用开机自动启动。

## 服务管理

以下命令在服务器上执行。

查看状态：

```bash
sudo systemctl status kalman-study
```

查看日志：

```bash
sudo journalctl -u kalman-study -n 80 --no-pager
```

重启服务：

```bash
sudo systemctl restart kalman-study
```

停止服务：

```bash
sudo systemctl stop kalman-study
```

备份章节和笔记：

```bash
sudo tar --exclude=.venv --exclude=study/.runtime --exclude=__pycache__ \
  -czf /var/lib/kalman-study/notebooks-backup-$(date +%Y%m%d-%H%M%S).tar.gz \
  -C /opt kalman-study
```

登录信息禁止提交到 Git。
登录令牌与密码具有相同的访问权限。
