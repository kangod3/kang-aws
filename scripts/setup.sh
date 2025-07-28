#!/bin/bash
set -e

# 1. 기존 main.py 프로세스 종료 (있을 경우)
pkill -f main.py || true
pkill -f anomaly_detect.py || true

# 2. 파일 이동
mv *.py ~/bpf-app/
mv model.pkl ~/bpf-app/

# 3. 실행
cd ~/bpf-app
nohup python3 main.py > output.log 2>&1 &
