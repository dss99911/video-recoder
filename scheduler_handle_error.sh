source /home/ec2-user/.bash_profile

sh "$RECORDER_PATH/scheduler.sh" > "$RECORDER_PATH/log/stdout$(date -d '+9 hour' +"%Y-%m-%dT%H:%M:%S").log" 2> "$RECORDER_PATH/log/stderr$(date -d '+9 hour' +"%Y-%m-%dT%H:%M:%S").log" \
  || sh "$RECORDER_PATH/send_to_slack.sh"