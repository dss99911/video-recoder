# RTMP stream download
1. find rtmp url
    - ex) rtmp://new_iradio.ebs.co.kr/iradio/iradiolive_m4a
    
2. use `rtmpdump` to download with flv file type
    - 

# HLS stream download
1. find m3u8 url
    - ex) 
   ```
   http://1fm.gscdn.kbs.co.kr/1fm_192_1.m3u8?Expires=1618215493&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cDovLzFmbS5nc2Nkbi5rYnMuY28ua3IvMWZtXzE5Ml8xLm0zdTgiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2MTgyMTU0OTN9fX1dfQ__&Signature=l2L~HoxlcldO471Ot8T1dLV6ZNh05HFj-Pb~eUY66IW~L8jJCX3n03QqD4xfYYXqSFKvR05YuPQYOIFEizNfYKLHHweJPzjEZuKk7dbRgHrR9IECiTi-sCxzzuODevxuScIJ5mcJppclKso2djKtM7dtwrxVD4nZmqyJ1wKLOc25feKY4jsJsvZZ0rBHxlJTBNh1Vg2~7Vj0fqCAapZOshwK6AsPaYySD5ip1IbFD2nOhQUYJ5zDo7YMjRAyrLdFlvDsLRHwPGCLhZBu9Bd~0QVJ1KjpvoeokKa-R0oeWiJC9nHFCG2TTSHn2TLIXLKoYyWUodQRSMDedPRYZm6N2Q__&Key-Pair-Id=APKAICDSGT3Y7IXGJ3TA
   ```
   
# Setup
1. upload [scheduler.sh](scheduler.sh), [video_recorder.py](video_recorder.py) to server by `scp` command
2. install youtube-dl, mmpeg. refer to [install.sh](install.sh)
3. configure crontab. set [crontab](crontab)

# Change time
1. crontab -e 
2. change cron `0 21 * * *` (it's UTC time)
3. change duration [scheduler.sh](scheduler.sh), `3600` is sec