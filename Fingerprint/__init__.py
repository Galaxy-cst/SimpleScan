from Fingerprint import startup


def start(num):
    starter = startup.setupone(num)
    return starter.find_one()
