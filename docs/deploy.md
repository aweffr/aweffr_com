# 部署 Ubuntu 20.04

python环境 3.8

- `apt install python3.8-dev mysql-client libmysqlclient-dev libssl-dev`
- `apt install python3-pip python3-venv python3-wheel`
- `cd /data && python3 -m venv aweffr_com_prod_venv`
  - venv生成后, python path = `/data/aweffr_com_prod_venv/bin/python`
- `source /data/aweffr_com_prod_venv/bin/activate`
- `cd /data/aweffr_com_prod && pip install -r requirements.txt`
- `export DJANGO_SETTINGS_MODULE=mysite.settings.prod`
- `cd /data/aweffr_com_prod && gunicorn mysite.wsgi --bind 127.0.0.1:9001 --workers 3`


## 参考使用gthread压测结果后的启动方式

https://yunsonbai.top/2017/06/15/gunicorn-django/

- `gunicorn mysite.wsgi -w 3 -b 127.0.0.1:9001 -k gthread --threads 4`
