import signal
import os
import subprocess
from datetime import datetime
import time

def __get_current_time(is_month):
    today_time = datetime.today()
    if is_month == 'month':
        return today_time.strftime("%Y%n%d")
    return today_time.strftime("%Y%m%d%H%M%S")

def his():
    file_name = __get_current_time("day") + "Download.mp4"
    absolute_path = "/Users/hyun.kim/workspace/projects/hyun/tbn-audio-recoder/output/" + file_name
    script = f"youtube-dl -o {absolute_path} http://radio2.tbn.or.kr:1935/daejeon/myStream/playlist.m3u8"
    process = subprocess.Popen(script,shell=True, preexec_fn=os.setsid)
    time.sleep(20)
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    subprocess.run(f"mv {absolute_path}.part {absolute_path}", stdout=subprocess.PIPE, shell=True)

if __name__ == "__main__":
    his()

