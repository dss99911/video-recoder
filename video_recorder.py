import argparse
from datetime import datetime, timedelta
import os
import signal
import subprocess

import time


def record_real_time_stream(video_url, output_path, duration):
    script = f"youtube-dl -o {output_path} {video_url}"

    try:
        process = subprocess.check_output(script, shell=True, preexec_fn=os.setsid)
        finish_time = datetime.now() + timedelta(0, int(duration))
        while datetime.now() < finish_time:
            time.sleep(5)
            if process.poll() is not None:  # terminated
                raise ValueError("Recording process terminated")
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        subprocess.run(f"mv {output_path}.part {output_path}", stdout=subprocess.PIPE, shell=True)
    except Exception as e:
        raise e


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-path", dest="output_path", action="store")  # extra value
    parser.add_argument("-d", "--duration", dest="duration", action="store")  # existence/nonexistence
    parser.add_argument("-v", "--video-url", dest="video_url", action="store")  # existence/nonexistence
    args = parser.parse_args()
    record_real_time_stream(args.video_url, args.output_path, args.duration)
