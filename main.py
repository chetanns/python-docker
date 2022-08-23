import time
import shutil
from datetime import datetime
from os.path import exists


def readFile(fileName):
    i = 0
    strTime = datetime.today().strftime('%Y%m%d_%H%M%S')

    while i == 0:
        if(exists(fileName)):
            with open(fileName, 'r') as file:
                [print(line.strip()) for line in file.readlines()]
            time.sleep(3)

            shutil.move(fileName, 'files/archived/Test_'+strTime+'.txt')
            time.sleep(3)
        else:
            print('No File exists')


readFile('files/current/Test.txt')
