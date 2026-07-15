#Timer test
import time
def timer(timer_time):
    for x in range(timer_time, 0, -1):
        seconds = x%60
        minutes = int((x/60)%60)
        hours = int(x/3600)%60
        print(f'{hours:02}:{minutes:02}:{seconds:02}')
        time.sleep(1)
    print('TIMES UP!')
timer(7200)