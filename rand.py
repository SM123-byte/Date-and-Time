import time

import random

def getRandomTime(startDate, endDate):
    print(f"Printing random date between {startDate} until {endDate}")
    randomgen = random.random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endTime = time.mktime(time.strptime(endDate,dateFormat))
    randomTime = startTime + randomgen * (endTime - startTime)
    randomdate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomdate

print("Random Date: ", getRandomTime('1/1/2020', '12/12/2024'))