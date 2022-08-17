source /home/ec2-user/.bash_profile

sh $RECORDER_PATH/scheduler.sh > $RECORDER_PATH/log/stdout.log 2> $RECORDER_PATH/log/stderr.log \
  || sh $RECORDER_PATH/send_to_slack.sh