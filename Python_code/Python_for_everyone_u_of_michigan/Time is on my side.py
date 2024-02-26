import math
nsecond = float(input('Amount of Seconds>>'))
hour = nsecond // 3600
minute = (nsecond - (hour*3600))//60
second: float = nsecond % 3600 % 60

print("Hour = " + str(math.trunc(hour)),
      "Minute = " + str(math.trunc(minute)),
      "Second = " + str(math.trunc(second)), sep='\n')
