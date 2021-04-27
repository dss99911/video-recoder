import argparse
import os
import signal
import subprocess

import time

def record_real_time_stream(video_url, output_path, duration):
    script = f"youtube-dl -o {output_path} {video_url}"
    process = subprocess.Popen(script, shell=True, preexec_fn=os.setsid)
    time.sleep(int(duration))
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    subprocess.run(f"mv {output_path}.part {output_path}", stdout=subprocess.PIPE, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-path", dest="output_path", action="store")  # extra value
    parser.add_argument("-d", "--duration", dest="duration", action="store")  # existence/nonexistence
    parser.add_argument("-v", "--video-url", dest="video_url", action="store")  # existence/nonexistence
    args = parser.parse_args()
    record_real_time_stream(args.video_url, args.output_path, args.duration)
