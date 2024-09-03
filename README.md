# Video Recorder

## Setup
run on linux AMD64 server. amazon linux 2023 is not working on ffmpeg, use amazon linux 2
```shell
wget https://raw.githubusercontent.com/dss99911/video-recoder/master/install_linux.sh
sh install_linux.sh {slack-webhook-url}
rm install_linux.sh
```

## Change time
- set UTC time. if your timezone is Seoul do Seoul time - 9, 
  - ex) 9am in Seoul -> set 0am
```shell
HOUR=10
MINUTE=30
DURATION=3600
sh $RECORDER_PATH/update_time.sh $HOUR $MINUTE $DURATION
# or
sh $RECORDER_PATH/update_time.sh 10 30 3600
```


## Update Source Code

```shell
sh $RECORDER_PATH/update_code.sh
```

## Enable/Disable
To disable : on `crontab -e`, remove scheduling code

To enable : on `crontab -e`, input scheduling code like [crontab](crontab)

