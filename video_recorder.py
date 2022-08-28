import argparse
import os
import signal
import subprocess
import time
from datetime import datetime, timedelta

import pytz
import requests


def record_real_time_stream(video_url, output_prefix, finish_time):
    if datetime.now() >= finish_time:
        return True

    output_path = get_output_path(output_prefix)

    script = f"youtube-dl -o {output_path} {video_url}"

    process = subprocess.Popen(script, shell=True, preexec_fn=os.setsid)
    # process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)

    while datetime.now() < finish_time:
        time.sleep(5)
        res = process.poll()
        if res is not None:  # terminated
            # out, err = process.communicate()
            raise ValueError(f"Recording process terminated")
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    subprocess.run(f"mv {output_path}.part {output_path}", stdout=subprocess.PIPE, shell=True)


def get_output_path(output_prefix):
    now = datetime.now(tz=pytz.timezone('Asia/Seoul'))
    time_str = now.strftime("%Y-%m-%dT%H:%M:%S")
    return f"{output_prefix}-{time_str}.mp4"


def send_slack_message(text, url="https://hooks.slack.com/services/00000/000000"):
    payload = {
        "text": text
    }
    requests.post(url, json=payload)


def retry_record(video_url, output_prefix, finish_time, slack_web_hook_url, count=15):
    try:
        record_real_time_stream(video_url, output_prefix, finish_time)
    except Exception as e:
        send_slack_message(f"video-recorder ERROR: {e}", slack_web_hook_url)
        time.sleep(60)
        retry_record(video_url, output_prefix, finish_time, slack_web_hook_url, count - 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-prefix", dest="output_prefix", action="store")
    parser.add_argument("-d", "--duration", dest="duration", action="store")
    parser.add_argument("-v", "--video-url", dest="video_url", action="store")
    parser.add_argument("-s", "--slack-web-hook-url", dest="slack_web_hook_url", action="store")
    args = parser.parse_args()
    finish_time = datetime.now() + timedelta(0, int(args.duration))
    print("duration:", args.duration, "finish_time:", finish_time)
    retry_record(args.video_url, args.output_prefix, finish_time, args.slack_web_hook_url)

