FROM ghcr.nju.edu.cn/home-assistant/aarch64-base:latest
# # 更新软件包列表
# RUN apk update
RUN echo "http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.21/main" > /etc/apk/repositories \
    && echo "http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.21/community" >> /etc/apk/repositories

# 更新软件包列表
RUN apk update
# # 安装 Nginx 和 Python3
RUN apk add --no-cache nginx python3 py3-pip 

# 创建虚拟环境并安装 Gunicorn
RUN python3 -m venv /venv \
    && . /venv/bin/activate \
    && pip install flask gunicorn

COPY init /init
RUN chmod +x /init

WORKDIR /var/www
# 拷贝 Flask 应用文件
COPY app.py /var/www/app.py

# 拷贝自定义的 Nginx 配置文件（如果有）
COPY default.conf /etc/nginx/http.d/default.conf

COPY iprouter /var/www/iprouter

# 启动 Nginx 和 Python 应用
CMD []