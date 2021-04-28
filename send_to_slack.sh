source /home/ec2-user/.bash_profile
curl -X POST -H 'Content-type: application/json' --data '{"text":"[ERROR] TBN Audio Record Failed!"}' $SLACK_WEBHOOK_URL