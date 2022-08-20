set -ex
HOUR=$1
MINUTE=$2
DURATION=$3

sed -i "s/RECORDER_DURATION=[0-9]*/RECORDER_DURATION=$DURATION/g" /home/ec2-user/.bash_profile

cat <<END | crontab -
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
$MINUTE $HOUR * * * sh $RECORDER_PATH/scheduler_handle_error.sh
END