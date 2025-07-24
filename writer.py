# influx_writer.py
from influxdb_client import InfluxDBClient, Point, WritePrecision

bucket = "bpf_detect"
org = "bpf_detector"
token = "hDDR2eRZ0oVt96bEbb55-Ew-Fx_BBcTd2x_A57Te1oE9DR6GwmIzQ5OqHXO6WInnWZ6ArMSvKu85AfAonR7zjw=="
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api()

def write_log(user, command, prediction, timestamp):
    point = (
        Point("audit_log")
        .tag("user", user)
        .field("command", command)
        .field("anomaly", int(prediction))
        .time(timestamp, WritePrecision.NS)
    )
    write_api.write(bucket=bucket, org=org, record=point)
