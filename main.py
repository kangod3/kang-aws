# main.py
import time
import os
from parser import parse_line
from detector import predict
from writer import write_log

AUDIT_LOG_PATH = "/var/log/audit/audit.log"
user = "root"  # 실제 사용자 파싱 시 교체

def tail_file(filename):
    with open(filename, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.2)
                continue
            yield line

if __name__ == "__main__":
    for line in tail_file(AUDIT_LOG_PATH):
        command = parse_line(line)
        if command:
            is_anomaly = predict(command)
            now_ns = int(time.time() * 1e9)
            write_log(user, command, is_anomaly, now_ns)
            print(f"[{'ANOMALY' if is_anomaly else 'OK'}] {command}")

