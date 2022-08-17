set -ex
HOUR=$1
MINUTE=$2
DURATION=$3

cat <<END | sudo tee /var/spool/cron/ec2-user
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
$MINUTE $HOUR * * * sh $RECORDER_PATH/scheduler_handle_error.sh
END

sed -i ''  "s/RECORDER_DURATION=[0-9]*/RECORDER_DURATION=$DURATION/g" /home/ec2-user/.bash_profile

sudo systemctl relad cron.service


