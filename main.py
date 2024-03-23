import subprocess, sys
from subprocess import Popen, PIPE
# 指定频道的URL
channel_url = "https://www.youtube.com/@Leader-Wu/featured"


exe_str = f"youtube-dl"
print(exe_str)
parent = subprocess.Popen([exe_str,channel_url,"playlist-end","1"], stderr=subprocess.PIPE)