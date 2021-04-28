RECORDER_PATH=/home/ec2-user/tbn-recorder
OUTPUT_PATH=/home/ec2-user/static
python3 $RECORDER_PATH"/video_recorder.py" -v http://radio2.tbn.or.kr:1935/daejeon/myStream/playlist.m3u8 -o ${OUTPUT_PATH}"/video-$(date -d '+9 hour' +"%Y-%m-%d").mp4" -d 7200