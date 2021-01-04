#!/usr/bin/python3

from osrs_api.const import AccountType
from osrs_api import Hiscores
import sys

modes = {
    'n': AccountType.NORMAL,
    'im': AccountType.IRONMAN,
    'hcim': AccountType.HARDCORE_IRONMAN,
    'uim': AccountType.ULTIMATE_IRONMAN
}

def main():
    username = sys.argv[1]
    mode = modes.get(sys.argv[2], AccountType.NORMAL) if len(sys.argv) == 3 else AccountType.NORMAL
    user = Hiscores(username, mode)
    output = open("out/total.txt", "w")
    output.write(str(user.total_level))
    output.close()
    for item in user.skills.items():
        output = open("out/"+item[0]+".txt", "w")
        output.write(str(item[1].level))
        output.close()

main()