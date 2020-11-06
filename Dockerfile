# pythonの最新版をベースに使用
FROM tiangolo/uvicorn-gunicorn-fastapi

# 作業ディレクトリ作成
WORKDIR /work

RUN apt-get update && apt-get install -y \
    sudo \
    python3-dev \
    python3-pip \
    libopencv-dev \
    opencv-data

# pipをアップグレード
RUN pip install --upgrade pip

COPY requirements.txt /work
RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]
