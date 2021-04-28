sh /home/ec2-user/tbn-recorder/scheduler.sh > /home/ec2-user/tbn-recorder/stdout.log 2> /home/ec2-user/tbn-recorder/stderr.log \
  || sh /home/ec2-user/tbn-recorder/send_to_slack.sh