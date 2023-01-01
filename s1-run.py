import os,signal

out = os.popen("ps aux | grep s1.py").read()

def pidkill(pid):
   try:
       a = os.kill(pid,signal.SIGKILL)
   except OSError:
       print("No such process!")

for line in out.splitlines():
    if's1.py' in line:
        pid = int(line.split()[1])
        print(pid)
    pidkill(pid)
    
os.system("python s1.py")
