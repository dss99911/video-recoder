source /home/ec2-user/.bash_profile
wget -O "$RECORDER_PATH/requirements.txt" https://raw.githubusercontent.com/dss99911/video-recoder/master/requirements.txt
wget -O "$RECORDER_PATH/scheduler.sh" https://raw.githubusercontent.com/dss99911/video-recoder/master/scheduler.sh
wget -O "$RECORDER_PATH/video_recorder.py" https://raw.githubusercontent.com/dss99911/video-recoder/master/video_recorder.py
wget -O "$RECORDER_PATH/scheduler_handle_error.sh" https://raw.githubusercontent.com/dss99911/video-recoder/master/scheduler_handle_error.sh
wget -O "$RECORDER_PATH/send_to_slack.sh" https://raw.githubusercontent.com/dss99911/video-recoder/master/send_to_slack.sh
wget -O "$RECORDER_PATH/update_time.sh" https://raw.githubusercontent.com/dss99911/video-recoder/master/update_time.sh

pip3 install -r requirements.txt