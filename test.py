import psutil
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB 설정
bucket = "my-bucket"
org = "my-org"
token = "wBM2Ah_2B00XIwu6MNzNEwtKmbwsKGBkR-YEanaIBebFCGPKxHO6fmm5e_b4dIOLK4EBnWId9Nvou4SHR_DbQQ=="
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

prev = psutil.net_io_counters()

while True:
    time.sleep(5)
    current = psutil.net_io_counters()
    sent = current.bytes_sent - prev.bytes_sent
    recv = current.bytes_recv - prev.bytes_recv

    point = (
        Point("net_traffic")
        .field("bytes_sent", sent)
        .field("bytes_recv", recv)
    )
    write_api.write(bucket=bucket, org=org, record=point)
    print(f"sent={sent} bytes, recv={recv} bytes")
    prev = current
