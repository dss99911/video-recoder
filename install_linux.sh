# add env path
set -xe

cat <<END | sudo tee -a /home/ec2-user/.bash_profile
SLACK_WEBHOOK_URL=$1
RECORDER_DURATION=7200
RECORDER_PATH=/home/ec2-user/tbn-recorder
RECORDER_OUTPUT_PATH=/home/ec2-user/static
END

source /home/ec2-user/.bash_profile

# install youtube-dl
sudo curl -L https://github.com/ytdl-org/youtube-dl/releases/download/2021.12.17/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

# install mmpeg
# https://www.maskaravivek.com/post/how-to-install-ffmpeg-on-ec2-running-amazon-linux/
# AMD64
wget https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-5.0.1-amd64-static.tar.xz
tar -xf ffmpeg-5.0.1-amd64-static.tar.xz
sudo mv ffmpeg-*-amd64-static/ /usr/local/bin/ffmpeg/
sudo ln -s /usr/local/bin/ffmpeg/ffmpeg /usr/bin/ffmpeg
rm ffmpeg-5.0.1-amd64-static.tar.xz

# download source code
mkdir "$RECORDER_PATH"
cd "$RECORDER_PATH"
mkdir log
wget https://raw.githubusercontent.com/dss99911/video-recoder/master/update_code.sh
sh update_code.sh

sudo yum install cronie -y
sudo systemctl start crond
sudo systemctl enable crond
pip3 install urllib3==1.26.16
sh update_time.sh 22 0 3600