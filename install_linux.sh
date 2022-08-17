# add env path
set -xe

cat <<END | sudo tee -a /home/ec2-user/.bash_profile
SLACK_WEBHOOK_URL=$1
RECORDER_DURATION=3600
RECORDER_PATH=/home/ec2-user/tbn-recorder
RECORDER_OUTPUT_PATH=/home/ec2-user/static
END

source /home/ec2-user/.bash_profile

# install youtube-dl
#sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
#sudo chmod a+rx /usr/local/bin/youtube-dl

# install mmpeg
# https://www.maskaravivek.com/post/how-to-install-ffmpeg-on-ec2-running-amazon-linux/
# AMD64
#wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
#tar -xf ffmpeg-release-amd64-static.tar.xz
#sudo mv /home/ec2-user/ffmpeg-*-amd64-static/ /usr/local/bin/ffmpeg/
#sudo ln -s /usr/local/bin/ffmpeg/ffmpeg /usr/bin/ffmpeg


# download source code
mkdir "$RECORDER_PATH"
cd "$RECORDER_PATH"
mkdir log
wget https://raw.githubusercontent.com/dss99911/video-recoder/master/scheduler.sh
wget https://raw.githubusercontent.com/dss99911/video-recoder/master/video_recorder.py
wget https://raw.githubusercontent.com/dss99911/video-recoder/master/scheduler_handle_error.sh
wget https://raw.githubusercontent.com/dss99911/video-recoder/master/send_to_slack.sh
wget https://raw.githubusercontent.com/dss99911/video-recoder/master/update_time.sh

sh update_time.sh 22 0 3600

sudo systemctl relad cron.service