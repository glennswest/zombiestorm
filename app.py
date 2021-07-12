import time
import subprocess

cmd_str = "sleep 5"
proc = subprocess.Popen([cmd_str], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
proc = subprocess.Popen([cmd_str], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
proc = subprocess.Popen([cmd_str], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
time.sleep(9000)
