from subprocess import Popen

p1 = Popen('/root/masscan/bin/masscan -p0-65535 120.79.214.167 --rate=500 -oJ 120.79.214.167', shell=True)

print(p1.communicate())
