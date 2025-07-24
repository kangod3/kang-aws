**BPF 도어 이상행위 탐지 시스템**

Linux 시스템의 실행 명령어를 실시간으로 감시하고, 머신러닝을 통해 비정상 행위를 탐지하여 InfluxDB 및 Grafana를 통해 시각화하는 이상행위 탐지 시스템

**프로젝트 개요**

auditd를 통해 시스템 실행 로그를 수집

머신러닝 모델을 활용해 명령어의 정상/비정상 여부 분류

탐지 결과를 InfluxDB에 기록

Grafana에서 실시간 시각화 대시보드를 제공

Python 기반의 경량 시스템으로, 클라우드 및 로컬 환경에서 모두 작동

**디렉토리 구조**
bpf-anomaly-detector/

├── simulate_writer.py # 정상/이상 명령어를 시뮬레이션하여 전송

├── main.py # 실시간 audit 로그를 분석하여 탐지

├── detector.py # 머신러닝 모델 훈련 및 예측

├── writer.py # InfluxDB에 로그 전송

├── train_example.py # 예제 학습 코드

├── requirements.txt # Python 의존성 목록

└── README.md # 프로젝트 설명서 (한글)

**설치 방법**

Python 패키지 설치
pip install -r requirements.txt

auditd 설정
sudo apt install auditd
sudo auditctl -a always,exit -F arch=b64 -S execve

**머신러닝 모델 학습**

python3 train_example.py

**명령어 시뮬레이션 실행**

python3 simulate_writer.py

simulate_writer.py는 정상 명령어와 이상 명령어를 혼합하여 무작위 전송

ml_detector.predict() 함수는 명령어의 비정상 여부를 판단하여 0(정상) 또는 1(이상)로 InfluxDB에 기록

**실시간 로그 탐지 실행**

python3 main.py

audit 로그를 실시간으로 읽고, 실행된 명령어 분석

**Grafana 시각화**

InfluxDB와 Grafana 연동

다음 쿼리를 활용해 시각화

from(bucket: "bpf_detect")
|> range(start: -5m)
|> filter(fn: (r) => r._measurement == "anomaly_detection")
|> filter(fn: (r) => r._field == "is_anomaly")

is_anomaly가 1이면 이상행위, 0이면 정상행위

**관련 기술**

auditd - Linux 커널 이벤트 로깅

InfluxDB - 시계열 데이터베이스

Grafana - 시각화 대시보드

Python - 전체 로직 구현

GitHub Actions - 자동화 및 테스트 
