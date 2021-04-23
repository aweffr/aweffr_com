# 部署 Ubuntu 20.04

python环境 3.8

- `apt install python3.8-dev mysql-client libmysqlclient-dev libssl-dev`
- `apt install python3-pip python3-venv python3-wheel`
- `python -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`
- `gunicorn mysite.wsgi --bind 127.0.0.1:9001 --workers 3`
