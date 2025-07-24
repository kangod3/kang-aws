# auditd_parser.py
import re

def parse_execve(line):
    # EXECVE 형식: a0="ps", a1="-e", ...
    matches = re.findall(r'a\d+="([^"]+)"', line)
    command = " ".join(matches)
    return command if command else None

def parse_line(line):
    if "type=EXECVE" in line:
        return parse_execve(line)
    return None
