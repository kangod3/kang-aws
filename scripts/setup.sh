#!/bin/bash
set -e

# 1. 시스템 패키지 설치
sudo apt update
sudo apt install -y influxdb grafana python3-pip

# 2. 서비스 활성화
sudo systemctl enable --now influxdb
sudo systemctl enable --now grafana-server

# 3. Python 라이브러리 설치
pip3 install --upgrade pip
pip3 install influxdb-client scikit-learn psutil

# 4. 디렉토리 준비 및 파일 이동
mkdir -p ~/bpf-app
mv *.py ~/bpf-app/
mv model.pkl ~/bpf-app/

# 5. 실행
cd ~/bpf-app
nohup python3 main.py > output.log 2>&1 &
