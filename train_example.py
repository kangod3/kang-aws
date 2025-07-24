# train_example.py
from detector import train_model

train_model([
    "ps -e -o pid,ppid,state,command",
    "ls -al /var/log",
    "cd /home",
    "cat /etc/passwd",
    "df -h",
    "uptime",
])
