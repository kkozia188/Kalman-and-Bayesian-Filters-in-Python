# Cloud JupyterLab configuration. Authentication files stay outside the repository.
from pathlib import Path

c.ServerApp.ip = "127.0.0.1"
c.ServerApp.port = 8890
c.ServerApp.port_retries = 0
c.ServerApp.open_browser = False
c.ServerApp.root_dir = "/opt/kalman-study"
c.ServerApp.base_url = "/kalman/"
c.ServerApp.default_url = "/lab/tree/02-Discrete-Bayes.zh-CN.ipynb"
c.ServerApp.trust_xheaders = True
c.ServerApp.allow_remote_access = True
c.IdentityProvider.token = Path("/etc/kalman-study/token").read_text().strip()
c.PasswordIdentityProvider.hashed_password = Path("/etc/kalman-study/password-hash").read_text().strip()
c.PasswordIdentityProvider.allow_password_change = False
