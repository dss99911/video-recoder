import argparse
import os
import signal
import subprocess
import time
from datetime import datetime, timedelta
import requests
import pytz


def record_real_time_stream(video_url, output_prefix, duration):
    finish_time = datetime.now() + timedelta(0, int(duration))

    if datetime.now() >= finish_time:
        return True

    output_path = get_output_path(output_prefix)

    script = f"youtube-dl -o {output_path} {video_url}"

    process = subprocess.check_output(script, shell=True, preexec_fn=os.setsid)

    while datetime.now() < finish_time:
        time.sleep(5)
        if process.poll() is not None:  # terminated
            raise ValueError("Recording process terminated")
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


def retry_record(args, count=30):
    try:
        record_real_time_stream(args.video_url, args.output_prefix, args.duration)
    except Exception as e:
        time.sleep(30)
        send_slack_message(str(e), args.slack_web_hook_url)
        retry_record(args, count - 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-prefix", dest="output_prefix", action="store")  # extra value
    parser.add_argument("-d", "--duration", dest="duration", action="store")  # existence/nonexistence
    parser.add_argument("-v", "--video-url", dest="video_url", action="store")  # existence/nonexistence
    parser.add_argument("-s", "--slack-web-hook-url", dest="slack_web_hook_url", action="store")  # existence/nonexistence
    args = parser.parse_args()

    retry_record(args)

