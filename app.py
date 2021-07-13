import time
import subprocess

print("Starting Python ZombieStorm")
cmd_str = "sleep 5"
print("Spawning Zombies")
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
