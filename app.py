import time
import subprocess

print("Starting Python ZombieStorm")
print("Spawning Zombies")
cmd_str="trap -- '' SIGINT SIGTERM;sleep 3"
proc = subprocess.Popen([cmd_str], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
proc = subprocess.Popen([cmd_str], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
proc = subprocess.Popen([cmd_str], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
proc = subprocess.Popen([cmd_str], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
proc = subprocess.Popen([cmd_str], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
time.sleep(90000000)
