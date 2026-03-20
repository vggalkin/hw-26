#!/usr/bin/python3
# -*- coding: utf-8

import subprocess
import platform

from ansible.plugins.lookup import lines


def check_ip(ip):
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        result = subprocess.run(
            ['ping', param, '1', ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3
        )
        return result.returncode == 0
    except:
        return False

def ips():
    with open('ips.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines

if __name__ == '__main__':
    for ip in ips():
        status = "ДОСТУПЕН" if check_ip(ip) else "НЕДОСТУПЕН"
        print(f"{ip}: {status}")
